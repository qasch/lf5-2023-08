import random

# Basisfunktionalität:
# - Nutzer soll aufgefordert werden, sechs Zahlen zwischen 1 und 49 einzugeben
# - Wir generieren zusätzlich sechs Zufallszahlen
# - Dann vergleichen wir, wieviele Übereinstimmungen es zwischen den eingegebenen und generierten Zahlen gibt
# - Das Ergebnis wird ausgegeben: "Du hast drei Richtige: 8, 23, 17"
#
# spätere Erweiterung:
# - Der Rechner spielt für uns soviele Spiele/Ziehungen, bis wir sechs Richtige haben
# - Wir zählen die Anzahl der Versuche und lassen uns dies als Ergebnis ausgeben: "Du hast 291874293874923874 Versuche gebraucht, um sechs Richtige zu erhalten" 

# Ideen zur Umsetzung:
# - Benutzereingabe über input()
# - Eingabe wird in einer List gespeichert 
# - Zu Beginn auf Eingabemöglichkeit verzichten, erst Logik implementieren, erst dann Eingabe und Validierung
# - Zufallszahlen mit dem Modul random generieren (muss importiert werden)
# - bei den generierten Zahlen darauf achten, dass es keine Dopplungen gibt
# - auch Zufallszahlen in Liste speichern
# - Zufallszahlen ausgeben
# - Vergleich der Eingabe mit den Zufallszahlen (wie genau machen wir das?)
# - Abschlussausgabe

# TODO: später über input() Benutzer nach den Zahlen fragen
# tipp = [8, 23, 17, 34, 3, 9]
# input() erzeugt immer einen String
benutzereingabe = input("Bitte gib sechs Zahlen zwischen 1 und 49 ein, jeweils durch ein Leerzeichen getrennt.\n")
# mit split() können wir einen String in seine Bestandteile zerlegen 
# und die einzelnen Elemente in eine Liste packen
# als Argument kann split() das Trennzeichen (Separator) übergeben werden
tipp = benutzereingabe.split(" ")    # erzeugt die Liste tipp mit den einzelnen Zahlen als Elemente

zufallszahlen = []
# Nutzung der anonymen Variable _, 
# da wir dies nur für die Definition brauchen, 
# aber nicht in unserem Code nutzen
# TODO: es kann passieren, dass wir zwei gleiche Zahlen der List hinzufügen -> korrigieren
for _ in range(6):       
    zufallszahlen.append(random.randint(1, 49))

# Listen sorieren
tipp.sort()
zufallszahlen.sort()

print("Tipp:", tipp)
print("Zufallszahlen:", zufallszahlen)

# nur zum Testen, später entfernen!
# zufallszahlen = [8, 21, 17, 33, 2, 9]

gewinnzahlen = []

# Für jedes Element von Tipp prüfen, ob es in der List zufallszahlen enthalten ist
for zahl in tipp:    
    if zahl in zufallszahlen:
        gewinnzahlen.append(zahl)

# Anzahl der richtigen Zahlen ermitteln
anzahl_richtige = len(gewinnzahlen)

print("Du hast folgende richtige Zahlen: {0} aus der Ziehung {1}".format(gewinnzahlen, zufallszahlen))
print(f"Du hast folgende {anzahl_richtige} richtige Zahlen: {gewinnzahlen} aus der Ziehung {zufallszahlen}")    # F-String, der konfortabelste Weg

# - Das Ergebnis wird ausgegeben: "Du hast drei Richtige: 8, 23, 17"





