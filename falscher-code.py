## Stromkosten gesamt (Kommentar, ein # wäre genug)
stromkostenGesamt = 500.00     # in Python ist der Punkt . das Dezimaltrennzeichen, nicht das Komma ,

'''Berechnung des Durchschnitts  

das hier ist ein Mehrzeiliger Kommentar
'''

durchschnitt = stromkostenGesamt / 12    # doppleter Slash //: Ganzzahliges Ergebnis einer Division 
"""Ausgabe"""  # auch ein mehrzeiliger Kommentar, wichtig sind drei " am Anfang und Ende

print(format(durchschnitt, ".2f"))     # durchschnitt auf zwei Nachkommastellen beschränkt

print("durchschnittliche Stromkosten pro Monat in Euro:", durchschnitt)


### zusätzliche Erklärungen:

var = ("hallo")      # Klammern sind syntaktisch nicht falsch aber unnötig
print(type(var))     # var ist vom Datentyp str
print(var)

foo = ("eins", "zwei")  # Klammern sind hier wichtig, um ein sog. Tuple zu erzeugen. Ein Tuple kann mehrere Werte aufnehmen
print(type(foo))
print(foo)