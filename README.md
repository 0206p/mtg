# MTG Kartenpool & Decks 🃏

🔗 **GitHub Repository:** [https://github.com/0206p/mtg](https://github.com/0206p/mtg)  
🌐 **Live Web-App (GitHub Pages):** [https://0206p.github.io/mtg/](https://0206p.github.io/mtg/)

---

Eine schlanke, webbasierte Single-Page-App zur Durchsuchung des gemeinsamen **Magic: The Gathering (MTG)** Kartenpools sowie zur Verwaltung und Prüfung der **Archidekt-Decks** von **Peter**, **Flo** und **Raphi**.

Die App läuft komplett im Browser (client-side) und lädt eure ManaBox-CSV-Exporte sowie eure synchronisierten Archidekt-Decks blitzschnell.

---

## 👥 Archidekt Profile

- 👤 **Peter:** [https://archidekt.com/u/p0206](https://archidekt.com/u/p0206) (10 Decks)
- 👤 **Flo:** [https://archidekt.com/u/Flogrim96](https://archidekt.com/u/Flogrim96) (26 Decks)
- 👤 **Raphi:** [https://archidekt.com/u/RaphaelOspelt](https://archidekt.com/u/RaphaelOspelt) (3 Decks)

---

## 🚀 Features

### 1. 🔍 Kartensuche & Filter
- **Live-Suche:** Schnelle Echtzeit-Suche nach Kartennamen im gesamten Pool (12.576 Versionen).
- **Multikriterien-Filter:**
  - **Edition (Set):** Automatisch aus allen vorhandenen Set-Codes generiert.
  - **Besitzer:** Filterbar nach *Peter*, *Flo* oder *Raphi*.
  - **Seltenheit (Rarity):** Common, Uncommon, Rare, Mythic, Special.
  - **Version / Finish:** Normal (Non-Foil), Foil ✨ und Etched.
  - **Sprache:** EN, DE, JA, etc.
- **Filter-Reset:** Ein-Klick-Button zum Zurücksetzen aller Filter.

### 2. 📷 Schwebende Bild-Vorschau (Hover)
- Jede Zeile verfügt über ein Kamera-Icon (📷).
- **Hover:** Beim Bewegen des Mauszeigers über das Kamera-Icon erscheint ein schwebendes Fenster mit dem hochauflösenden Original-Kartenbild von Scryfall. Es folgt der Maus und öffnet keine störenden Links.

### 3. 🛒 Cardmarket-Verlinkung
- Jeder Kartenname ist direkt als anklickbarer **Cardmarket-Link** formatiert und öffnet die deutsche Suche nach dieser Karte mit einem Klick.

### 4. 🎴 Deck-Zugehörigkeit („In Decks“)
- In der Kartensuche und im Deck-Checker zeigt eine eigene Spalte sofort an, **in welchen Decks eine Karte bereits verbaut ist** (inklusive Besitzer-Badge des Decks).
- Filterbar: Filter, um gezielt nur unbenutzte ("freie") Karten oder nur in Decks verbaute Karten anzuzeigen.

### 5. 🎴 Archidekt Decks (39 Decks integriert!)
- **Schlanke Deck-Karten:** Jedes Deck wird übersichtlich mit seinem **Commander als Haupttitel** (👑), Format und Kartenzahl dargestellt.
- **Filter & Suche:** Nach Decknamen, Commander oder Besitzer filtern.
- **1-Klick Deckprüfung:** Klicke bei einem beliebigen Deck auf **„⚡ Im Deck-Checker prüfen“** – die vollständige Deckliste wird automatisch geladen und sofort gegen euren Kartenpool abgeglichen!
- **Archidekt-Direktlink:** Direkter Sprung zum Deck auf archidekt.com.

### 6. 📋 Deck- & Listen-Checker
- Eigener Tab zum Einfügen kompletter Decklisten (z. B. aus MTG Arena, Moxfield, Archidekt oder Textdateien).
- **Schnellauswahl:** Wähle direkt aus einem Dropdown eines eurer 39 Archidekt-Decks aus.
- **Dashboard & Auswertung:**
  - Gesamtanzahl gesuchter Karten, im Pool vorhandene Karten, fehlende Karten und Abdeckung in Prozent (mit visuellem Fortschrittsbalken).
  - Aufschlüsselung pro Karte: Wer hat sie und wie oft (`Peter 2x`, `Flo 1x`)?
  - Statusanzeige: *Komplett*, *Fehlt Xx*, *Fehlt komplett*.
  - Direkte Cardmarket-Links für jede Karte (insbesondere zum Nachbestellen fehlender Karten).

---

## 📁 Projektstruktur

```text
mtg/
├── index.html        # Web-App (HTML, CSS Dark Theme, Vanilla JS)
├── decks.json        # Synchronisierte Archidekt-Decks mit allen Kartenlisten
├── sync_decks.py     # Python-Script zum automatischen Abgleich mit Archidekt
├── peter.csv         # ManaBox-Export von Peter (~5.029 Versionen)
├── flo.csv           # ManaBox-Export von Flo (~6.190 Versionen)
├── raphi.csv         # ManaBox-Export von Raphi (~1.357 Versionen)
└── README.md         # Dokumentation
```

---

## 🔄 Sammlungen & Decks aktualisieren

### 1. Archidekt-Decks synchronisieren
Um neu erstellte oder geänderte Decks von euren Archidekt-Profilen zu aktualisieren, führe einfach aus:
```bash
python sync_decks.py
```
Das Skript lädt alle 39+ Decks inklusive aller Kartenlisten direkt von Archidekt herunter und aktualisiert die Datei `decks.json`.

### 2. ManaBox-Sammlungen aktualisieren
1. In **ManaBox** die Sammlung als CSV exportieren.
2. Die Datei ersetzen als `peter.csv`, `flo.csv` oder `raphi.csv`.
3. Änderungen committen und pushen:
   ```bash
   git add *.csv decks.json
   git commit -m "Update Sammlungen und Decks"
   git push origin main
   ```
