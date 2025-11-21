# Zahlensystem-Konverter (GUI)

Eine Desktop-Anwendung zur bidirektionalen Umrechnung zwischen Dezimal- und Dualsystem (Binärsystem), entwickelt mit Python und PyQt5.

## Aufgabenstellung
Entwicklung eines Programms mit grafischer Oberfläche, das folgende Funktionen bietet:
1.  **Dezimal zu Dual:** Umrechnung einer Ganzzahl in ihre binäre Darstellung.
2.  **Dual zu Dezimal:** Umrechnung einer Binärfolge (nur 0 und 1) in eine Dezimalzahl.
3.  **Dokumentation:** Explizite Begründung des gewählten Lösungsansatzes im Quellcode.

## Technische Umsetzung & Lösungsansatz
Der Code verfolgt den Ansatz "Built-in over Custom Implementation" für maximale Robustheit und Performance:

*   **Konvertierungslogik:**
    *   Dezimal → Dual: Nutzung der nativen `bin()` Funktion inkl. String-Slicing (`[2:]`) zum Entfernen des `0b`-Präfixes.
    *   Dual → Dezimal: Nutzung von `int(string, 2)` zur Interpretation zur Basis 2.
*   **Validierung:**
    *   Prüfung auf nicht-binäre Zeichen bei der Dual-Eingabe.
    *   Ausschluss negativer Zahlen für diesen speziellen Anwendungsfall.
    *   Fehlerausgabe via `QMessageBox`.
*   **GUI-Architektur:** Saubere Trennung von UI-Design (`.ui`-Datei) und Anwendungslogik (`.py`-Datei).

## Dateistruktur
*   `main_app.py`: Die Hauptanwendung mit der Konvertierungslogik.
*   `converter.ui`: Das GUI-Design (Qt Designer).
*   `ui_converter.py`: Das kompilierte User Interface.

## Installation & Start
Voraussetzung: Python 3.x und PyQt5.

Installation:
```bash
pip install PyQt5
