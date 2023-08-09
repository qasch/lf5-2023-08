# Lists in Python
# in einer List (Array in anderen Sprachen) können mehrere Elemente abgelegt werden
# die Elemente können von unterschiedlichen Datentypen sein
# die List ist geordnet / einzelene Elemente können über eine Index angesprochen werden
# der Index beginnt immmer mit der Null 0, nicht mit der 1
# das erste Element einer Liste steht also immer am Index 0

digits_str = "1 34 8 27"
print(digits_str)
print(type(digits_str))

digits_list = [1, 34, 8, 27]
print(digits_list)
print(type(digits_list))

string_list = ["Banana", "Apple", "Orange"]
print(string_list)
print(type(string_list))

## einzelne Elemente einer List ausgeben lassen (über den Index)
# Index         0     1       2       3
mixed_list = [True, 2.34, "hallo du", 7]
print(mixed_list)
print(type(mixed_list))
print(mixed_list[2])  # 3. Element
print(mixed_list[0])  # 1. Element
# Wird ein negativer Index angegeben, fangen wir von hinten an zu zählen
# das letzte Element wird über -1 referenziert
print(mixed_list[-1])  # letzes Element
print(mixed_list[-2])  # vorletzes Element

print(string_list[1])

print(mixed_list[:3])    # alle Element bis zum Index 3
print(mixed_list[3:])    # alle Element ab Index 3
print(mixed_list[::])    # alle Elemente der List
print(mixed_list[::3])   # Index 0 und Index 3
print(mixed_list[::-3])  # letzer Index und von dort 3 Elemente nach vorne



## Alle Elemente einer List ausgeben lassen
colours = ["green", "orange", "black", "red"]

print("Es gibt folgende Farben: {0}".format(colours))
print("Es gibt folgende Farben:\n {0}\n {1}\n {2}\n {3}".format(colours[0], colours[1], colours[2], colours[3]))

# while Loop zur Ausgabe aller Farben:
print("\nAlle Elemente von colours mit while Loop:")    
index = 0    
while index <= 3:
    print(colours[index])
    index += 1

## Beim Versuch auf einen Index zuzugreifen, den es nicht gibt, kommt es zu einer Fehlermeldung:
##  IndexError: list index out of range    (häufig auftretender Fehler)
# index = 0    
# while index <= 4:
#     print(colours[index])
#     index += 1

# print(colours[10])


# for Loop zur Ausgabe aller Elemente:
print("\nAusgabe aller Elemente von colours mit for Loop:")    
for colour in colours:
    print(colour)

# List mit den Zahlen von 1 bis 100
print("\nList mit den Zahlen von 1 bis 100")
some_numbers = []
for number in range(100):
    some_numbers.append(number)

print(some_numbers)

# Elemente aus Listen entfernen
# Liste wird verändert
## pop
some_numbers.pop()    # letztes Element aus der Liste entfernen (99)
print(some_numbers)

some_numbers.pop(-1)    # letztes Element aus der Liste entfernen (99)
print(some_numbers)

some_numbers.pop(0)   # Element am Index 0 entfernen
print(some_numbers)

some_numbers.pop(-2)   # vorletztes Element entfernen
print(some_numbers)

## remove
animals = ["Hund", "Katze", "Maus", "Affe", "Igel"]
# animals.pop(3)
animals.remove("Igel")
print(animals)
## führt zu Fehler:
# animals.remove("Eichhörnchen")
# print(animals)
# animals.pop(5)
# print(animals)

## Sortieren
animals.sort()
print(animals)

# "Bär" an zweiter Position in die List einfügen
animals.insert(1, "Bär")
print(animals)

animals.insert(1, "Vogel")
print(animals)

## Element in Liste ersetzen
animals[1] = "Schlange"
print(animals)

# Anzahl der Elemente der Liste ausgeben
print(len(animals))

# enumerate()
# Alle Elemente mit zugehörigem Index ausgeben lassen
for index, animal in enumerate(animals):
    print(index, animal)

