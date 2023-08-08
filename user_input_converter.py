# TODO: 
# - [x] Möglichkeit, nach falscher Eingabe neue Eingabe zu tätigen    
# - [ ] evtl. Problem falls Float eingegeben wird. Prüfung möglich?
# - [x] Code besser strukturieren/aufräumen

# Variablen, die im gesamten Code gültig sind
umrechung_stunden = 24
umrechung_minuten = 24 * 60
umrechung_sekunden = 24 * 60 * 60

# Funktionsdeklarationen
def umrechnung_tage_in_stunden(anzahl_tage):
    print(str(anzahl_tage) + " Tage sind " + str(anzahl_tage * umrechung_stunden) + " Stunden.")

def benutzereingabe_pruefen(anzahl_tage):

    if anzahl_tage.isdigit():

        anzahl_tage = int(anzahl_tage)

        if anzahl_tage > 0:
            umrechnung_tage_in_stunden(anzahl_tage)
            #continue     # an dieser Stelle springen wir wieder an den Anfang der Schleife
            #break       # an dieser Stelle wird die Schleife verlassen
        elif anzahl_tage == 0:
            print("Die eingegebene Zahl ist gleich 0, das Ergebnis kennst du selbst...")
        else:
            print("Die eingegebene Zahl ist kleiner als 0, Konvertierung nicht möglich.")

    else:
        print("Bitte nur ganze Zahlen eingeben und keinen Quatsch!")

# eigentlicher Programmablauf / Aufruf der Funktionen in einer Schleife
# Schleife solange durchlaufen, wie kein "Ende" eingegeben wird
anzahl_tage = ""
while anzahl_tage != "Ende":      # bewusst erstellte Endlosschleife
    anzahl_tage = input("Bitte gib die Anzahl der Tage an, die konvertiert werden sollen.\n")   # lokale Variable (nur in der Funktion bekannt)
    benutzereingabe_pruefen(anzahl_tage)

print("Programm beendet")
