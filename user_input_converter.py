# TODO: 
# - Möglichkeit, nach falscher Eingabe neue Eingabe zu tätigen    
# - evtl. Problem falls Float eingegeben wird. Prüfung möglich?
# - Code besser strukturieren/aufräumen

def umrechnung_tage_in_stunden():
    print(str(anzahl_tage) + " Tage sind " + str(anzahl_tage * umrechung_stunden) + " Stunden.")

umrechung_stunden = 24
umrechung_minuten = 24 * 60
umrechung_sekunden = 24 * 60 * 60

# while - Start
while True:      # bewusst erstellte Endlosschleife
    anzahl_tage = input("Bitte gib die Anzahl der Tage an, die konvertiert werden sollen.\n")

    if anzahl_tage.isdigit():

        anzahl_tage = int(anzahl_tage)

        if anzahl_tage > 0:
            umrechnung_tage_in_stunden()
            break       # an dieser Stelle wird die Schleife verlassen
        elif anzahl_tage == 0:
            print("Die eingegebene Zahl ist gleich 0, das Ergebnis kennst du selbst...")
        else:
            print("Die eingegebene Zahl ist kleiner als 0, Konvertierung nicht möglich.")

    else:
        print("Bitte nur ganze Zahlen eingeben und keinen Quatsch!")

# while - Ende

print("Programm beendet")
