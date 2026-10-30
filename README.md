# MTG Kartenpool 🃏

🔗 **GitHub Repository:** [https://github.com/0206p/mtg](https://github.com/0206p/mtg)  
🌐 **Live Web-App (GitHub Pages):** [https://0206p.github.io/mtg/](https://0206p.github.io/mtg/)

---

Eine schlanke, webbasierte Single-Page-App zur Durchsuchung und Verwaltung des gemeinsamen **Magic: The Gathering (MTG)** Kartenpools von **Peter**, **Flo** und **Raphi**.

Die App läuft komplett im Browser (client-side) und lädt die ManaBox-CSV-Exporte der drei Sammlungen direkt und performant via PapaParse.

---

## 🚀 Features

### 1. 🔍 Kartensuche & Filter
- **Live-Suche:** Schnelle Echtzeit-Suche nach Kartennamen.
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

### 3. 🔗 Scryfall- & Cardmarket-Integration
- **Scryfall ↗:** Direkter Link zur exakten Kartenversion auf Scryfall.
- **Cardmarket ↗:** Direkte Suche auf Cardmarket mit einem Klick zum Kaufen/Preise prüfen.

### 4. 📋 Deck- & Listen-Checker
- Eigener Tab zum Einfügen kompletter Decklisten (z. B. aus MTG Arena, Moxfield, Archidekt oder Textdateien).
- **Unterstützte Formate:**
  - `1 Sol Ring`
  - `4 Lightning Bolt`
  - `1 Demonic Tutor (BLB) 250`
  - `Counterspell`
- **Dashboard & Auswertung:**
  - Gesamtanzahl gesuchter Karten, vorhandene Karten, fehlende Karten und Abdeckung in Prozent (mit visuellem Fortschrittsbalken).
  - Aufschlüsselung pro Karte: Wer hat sie und wie oft (`Peter 2x`, `Flo 1x`)?
  - Statusanzeige: *Komplett*, *Fehlt Xx*, *Fehlt komplett*.
  - Direkte Cardmarket-Links für jede Karte (insbesondere zum Nachbestellen fehlender Karten).

---

## 📁 Projektstruktur

```text
mtg/
├── index.html     # Komplette Web-App (HTML, CSS Dark Theme, Vanilla JS)
├── peter.csv      # ManaBox-Export von Peter (~5.029 Versionen)
├── flo.csv        # ManaBox-Export von Flo (~6.190 Versionen)
├── raphi.csv      # ManaBox-Export von Raphi (~1.357 Versionen)
└── README.md      # Diese Dokumentation
```

---

## 🔄 Sammlungen aktualisieren

1. In **ManaBox** (oder deiner Sammlungs-App) die Sammlung als CSV exportieren.
2. Die Datei umbenennen in:
   - `peter.csv`
   - `flo.csv`
   - `raphi.csv`
3. Im Repository ersetzen und committen/pushen:
   ```bash
   git add *.csv
   git commit -m "Update Sammlungen"
   git push origin main
   ```
4. Die Web-App aktualisiert die Bestände automatisch beim nächsten Laden.
