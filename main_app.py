""" *****************************************************************************
Aufgabe 9 Hauptdatei: GUI-Steuerung und Logik-Verbindung, Zahlensystem-Konverter 
******************************************************************************"""

# =====================================================================================
# Dokumentation des Ansatzes
# =====================================================================================
# Der gewaehlte Ansatz basiert auf der Nutzung der eingebauten Python-Funktionen
# fuer die Zahlensystemkonvertierung. Dies ist der einfachste, kuerzeste und 
# fehlerresistenteste Weg fuer diese Aufgabenstellung.
#
# 1. Dezimal (int) zu Dual (String):
#    - Funktion: bin(zahl)
#    - Vorgehen: str(bin(zahl))[2:] wird verwendet, um das Praefix '0b' zu entfernen.
#
# 2. Dual (String) zu Dezimal (int):
#    - Funktion: int(string, basis)
#    - Vorgehen: int(dual_string, 2) wird verwendet, wobei die Basis 2 die 
#      korrekte Interpretation des binaeren Eingabestrings sicherstellt.
#
# GUI-Implementierung:
# Die grafische Oberflaeche wurde mit Qt Designer erstellt und das Layout in
# die Datei 'ui_converter.py' konvertiert. PyQt5 dient als GUI-Bibliothek.
# Einfache Fehlerbehandlung (ValueError) und eine Funktion zum Leeren der Felder 
# sind implementiert.
# ===================================================================================

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Import der automatisch generierten GUI-Klasse
from ui_converter import Ui_MainWindow 

class ZahlConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Initialisierung der Anwendung und Verbindung der GUI-Elemente."""
        super().__init__()
        # Initialisiert das Layout aus der konvertierten ui_converter.py
        self.setupUi(self)
        
        # Setzt den Fenstertitel des Hauptfensters
        self.setWindowTitle("Zahlensystem Rechner")
        
        # --- Signale und Slots verbinden ---
        # Verbindet den Klick des Dez->Dual-Buttons mit der Methode dez_zu_dual
        self.btn_dez_zu_dual.clicked.connect(self.dez_zu_dual)
        # Verbindet den Klick des Dual->Dez-Buttons mit der Methode dual_zu_dez
        self.btn_dual_zu_dez.clicked.connect(self.dual_zu_dez)
        # Verbindung fuer den Loeschbutton
        self.btn_clear.clicked.connect(self.clear_fields) 

    def dez_zu_dual(self):
        """Umrechnungslogik: Dezimalzahl (lineEdit_dezimal) in Dualzahl umwandeln."""
        try:
            # Eingabe holen und in Ganzzahl umwandeln
            dezimal_str = self.lineEdit_dezimal.text()
            dezimal_zahl = int(dezimal_str)

            if dezimal_zahl < 0:
                 # Hinweis: Fuer negative Zahlen waere das Zweierkomplement notwendig.
                 # Hier wird nur die Konvertierung positiver Zahlen unterstuetzt.
                 raise ValueError("Nur positive Zahlen werden direkt unterstuetzt.")
            
            # Kern-Umrechnung: Entfernt '0b' mit [2:]
            dual_str = bin(dezimal_zahl)[2:]

            # Ergebnis in das Dual-Feld schreiben
            self.lineEdit_dual.setText(dual_str)
        except ValueError as e:
            # Fehlerbehandlung bei ungueltiger Eingabe (z.B. Text statt Zahl)
            QMessageBox.critical(self, "Eingabefehler", 
                                 f"Ungueltige Dezimalzahl: {e}")
            self.lineEdit_dual.setText("")
            
    def dual_zu_dez(self):
        """Umrechnungslogik: Dualzahl (lineEdit_dual) in Dezimalzahl umwandeln."""
        try:
            # Eingabe holen
            dual_str = self.lineEdit_dual.text()
            
            # Validierung: Pruefen, ob der String nur '0' und '1' enthaelt
            if not all(c in '01' for c in dual_str):
                 raise ValueError("Dualzahl darf nur 0 und 1 enthalten.")

            # Kern-Umrechnung: int(string, basis) mit Basis 2
            dezimal_zahl = int(dual_str, 2)

            # Ergebnis in das Dezimal-Feld schreiben
            self.lineEdit_dezimal.setText(str(dezimal_zahl))
        except ValueError as e:
            # Fehlerbehandlung bei ungueltiger Eingabe (z.B. Zeichen, die keine 0/1 sind)
            QMessageBox.critical(self, "Eingabefehler", 
                                 f"Ungueltige Dualzahl: {e}")
            self.lineEdit_dezimal.setText("")

    def clear_fields(self):
        """Leert alle Textfelder (Dezimal und Dual) bei Klick auf 'Alles loeschen'."""
        self.lineEdit_dezimal.setText("")
        self.lineEdit_dual.setText("")


if __name__ == '__main__':
    # Standard-PyQt5-Code zum Starten der Anwendung
    app = QApplication(sys.argv)
    converter = ZahlConverterApp()
    converter.show()
    sys.exit(app.exec_())
    
    
    
# =============================================================================
# Projektdokumentation: Zahlensystem-Konverter
# =============================================================================

# gewaehlter Ansatz (Kuerzeste und Robusteste Loesung)
# -----------------------------------------------------------------------------
# Der gewaehlte Ansatz basiert auf der direkten Nutzung der eingebauten
# Funktionen der Python-Standardbibliothek, um die Konvertierung so
# effizient und fehlerresistent wie moeglich zu halten.
#
# 1. Dezimal zu Dual (Binaer):
#    - Funktion: bin()
#    - Vorgehen: Die Funktion bin(zahl) konvertiert die Ganzzahl in einen
#      binaeren String. Das Praefix '0b' (z.B. bei bin(10) → '0b1010')
#      wird mittels String-Slicing ([2:]) entfernt, um die reine Dualzahl
#      zu erhalten.
#
# 2. Dual (Binaer) zu Dezimal:
#    - Funktion: int(string, basis)
#    - Vorgehen: Die Funktion int() wird mit dem binaeren String und der
#      expliziten Angabe der Basis 2 (int(dual_string, 2)) aufgerufen.
#      Dies interpretiert den String korrekt als Binaerzahl.
#
# -----------------------------------------------------------------------------
# Projektstruktur
# -----------------------------------------------------------------------------
# Das Projekt besteht aus zwei Hauptdateien:
# 1. ui_converter.py: Die von Qt Designer generierte Layout-Klasse.
# 2. main_app.py: Die Hauptanwendungsklasse, die die Konvertierungslogik
#    implementiert, die UI-Elemente verbindet (mittels Signals/Slots)
#    und eine einfache Fehlerbehandlung (try-except/QMessageBox) beinhaltet.
#    Zusaetzlich wurde die Methode clear_fields() implementiert und mit dem
#    Button btn_clear verbunden, um die Eingabefelder zu leeren und die 
#    Benutzerfreundlichkeit zu erhoehen.
# =============================================================================