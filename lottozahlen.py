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
# - auch Zufallszahlen in Liste speichern
# - Zufallszahlen ausgeben
# - Vergleich der Eingabe mit den Zufallszahlen (wie genau machen wir das?)
# - Abschlussausgabe