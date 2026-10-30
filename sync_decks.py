"""
Script to synchronize Archidekt decks for Peter, Flo, and Raphi into decks.json.
Run this script whenever you want to update your Archidekt decks locally:
    python sync_decks.py
"""

import urllib.request
import re
import json
import concurrent.futures
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*'
}

USERS = [
    {'name': 'Peter', 'username': 'p0206', 'badge': 'owner-peter'},
    {'name': 'Flo', 'username': 'Flogrim96', 'badge': 'owner-flo'},
    {'name': 'Raphi', 'username': 'RaphaelOspelt', 'badge': 'owner-raphi'}
]

FORMAT_NAMES = {
    1: 'Standard',
    2: 'Modern',
    3: 'Commander / EDH',
    4: 'Legacy',
    5: 'Vintage',
    6: 'Pauper',
    7: 'Custom',
    8: 'Pioneer',
    9: 'Historic',
    10: 'Brawl',
    11: 'Oathbreaker',
    12: 'Premodern',
    13: 'Tiny Leaders',
    14: 'Duel Commander',
    15: 'Gladiator',
    16: 'Casual'
}

def fetch_user_deck_metadata(user):
    username = user['username']
    url = f"https://archidekt.com/u/{username}"
    print(f"Fetching profile for {user['name']} ({username})...")
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html)
        if not m:
            print(f"  Warning: __NEXT_DATA__ not found for {username}")
            return []
        
        data = json.loads(m.group(1))
        props = data.get('props', {}).get('pageProps', {})
        user_obj = props.get('user', {})
        decks = user_obj.get('decks', [])
        
        results = []
        for d in decks:
            format_id = d.get('deckFormat', 3)
            results.append({
                'id': d.get('id'),
                'name': d.get('name'),
                'owner': user['name'],
                'ownerUsername': username,
                'badge': user['badge'],
                'formatId': format_id,
                'formatName': FORMAT_NAMES.get(format_id, 'Commander / EDH'),
                'updatedAt': d.get('updatedAt'),
                'colors': d.get('colors', {}),
                'archidektUrl': f"https://archidekt.com/decks/{d.get('id')}"
            })
        print(f"  Found {len(results)} decks for {user['name']}.")
        return results
    except Exception as e:
        print(f"  Error fetching profile {username}: {e}")
        return []

def fetch_deck_details(deck_meta):
    deck_id = deck_meta['id']
    url = f"https://archidekt.com/api/decks/{deck_id}/"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            deck_data = json.loads(resp.read().decode('utf-8'))
        
        cards = deck_data.get('cards', [])
        parsed_cards = []
        commanders = []
        total_count = 0

        for c in cards:
            qty = c.get('quantity', 1)
            categories = c.get('categories', [])
            card_info = c.get('card', {})
            oracle = card_info.get('oracleCard', {})
            name = oracle.get('name') or card_info.get('name') or "Unknown"
            
            # Check for commander
            is_commander = any(cat.lower() == 'commander' for cat in categories)
            if is_commander and name not in commanders:
                commanders.append(name)
            
            # Only count main deck (ignore Maybeboard / Sideboard in main count if needed, or include)
            is_maybeboard = any(cat.lower() in ['maybeboard', 'sideboard', 'scratchpad'] for cat in categories)
            if not is_maybeboard:
                total_count += qty

            parsed_cards.append({
                'name': name,
                'quantity': qty,
                'categories': categories,
                'isCommander': is_commander,
                'isMaybeboard': is_maybeboard
            })

        deck_meta['cardCount'] = total_count
        deck_meta['commanders'] = commanders
        deck_meta['cards'] = parsed_cards
        print(f"  Loaded deck: {deck_meta['name']} ({total_count} cards)")
        return deck_meta
    except Exception as e:
        print(f"  Failed loading cards for deck {deck_id} ({deck_meta['name']}): {e}")
        deck_meta['cardCount'] = 0
        deck_meta['commanders'] = []
        deck_meta['cards'] = []
        return deck_meta

def main():
    print("=== MTG ARCHIDEKT SYNC ===")
    all_deck_metas = []
    for user in USERS:
        metas = fetch_user_deck_metadata(user)
        all_deck_metas.extend(metas)
    
    print(f"\nFetching details for {len(all_deck_metas)} total decks...")
    
    full_decks = []
    # Use ThreadPoolExecutor to fetch decks concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        future_to_deck = {executor.submit(fetch_deck_details, d): d for d in all_deck_metas}
        for future in concurrent.futures.as_completed(future_to_deck):
            res = future.result()
            full_decks.append(res)
    
    # Sort decks: first by Owner (Peter, Flo, Raphi), then by Name
    owner_order = {'Peter': 1, 'Flo': 2, 'Raphi': 3}
    full_decks.sort(key=lambda d: (owner_order.get(d['owner'], 9), d['name'].lower()))

    output_data = {
        'lastSync': time.strftime('%Y-%m-%d %H:%M:%S'),
        'totalDecks': len(full_decks),
        'owners': {
            'Peter': {'username': 'p0206', 'url': 'https://archidekt.com/u/p0206', 'count': sum(1 for d in full_decks if d['owner'] == 'Peter')},
            'Flo': {'username': 'Flogrim96', 'url': 'https://archidekt.com/u/Flogrim96', 'count': sum(1 for d in full_decks if d['owner'] == 'Flo')},
            'Raphi': {'username': 'RaphaelOspelt', 'url': 'https://archidekt.com/u/RaphaelOspelt', 'count': sum(1 for d in full_decks if d['owner'] == 'Raphi')}
        },
        'decks': full_decks
    }

    with open('decks.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nSUCCESS: Saved {len(full_decks)} decks into decks.json!")

if __name__ == '__main__':
    main()

