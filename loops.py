# Loops in Python

## while-Loop
## Bei einem while-Loop müssen wir darauf achten, ausserhalb der Schleife eine Zählvariable zu erstellen (number)
## und diese Zählvariable muss innerhalb verändert werden (erhöht, erniedrig, etc.)

### Gib die Zahlen 1 bis 10 aus
print("While-Loop: Ausgabe der Zahlen von 1 bis 10")
number = 1
while number <= 10:
    print(number)
    # number = number + 1
    number += 1      # increment, in anderen Sprachen z.B. number++

### While-Loop mit else
print("\nWhile-Loop mit else")
number = 1
while number <= 10:
    print(number)
    number += 1      # increment, in anderen Sprachen z.B. number++
else:
    print("Es wurden {0} Elemente ausgegeben".format(number - 1))

### break
print("\nWhile-Loop mit break")
number = 1
while number <= 100:
    print(number)     # 19
    number += 1       # 20
    if number == 20:
        break       # Schleife wird hier verlassen

# continue
# Ausgabe aller ungeraden Zahlen zwischen 0 und 20
print("\nWhile-Loop mit continue")
number = 0
while number < 20:
    number += 1
    if number % 2 == 0:
        continue    # wir springen zum Anfang der Schleife und führen diese erneut aus
    print(number)

## for-Loop
## Bei for-Loops brauchen wir keine extra Zählvariable ausserhalb der Schleife zu erstellen, 
## dies passiert in der Definition der Schleife (count)
## Auch müssen wir keine Zählvariable verändern, der for-Loop erledigt das für uns und erkennt
## automatisch das Ende einer Iteration

### Ausgabe der Zahlen von 0 bis 9
print("\nFor-Loop: Ausgabe der Zahlen von 0 bis 9")
for count in range(10):      # range(start, ende)  start ist inklusiv, ende exklusiv
    print(count)
    
### Ausgabe der Zahlen von 1 bis 10
print("\nFor-Loop: Ausgabe der Zahlen von 1 bis 10")
for count in range(1,11):      # range(start, ende)  start ist inklusiv, ende exklusiv
    print(count)
    
### range()
print("\nFor-Loop: Ausgabe der ungeraden Zahlen von 1 bis 10")
for count in range(1,11,2):    # range(start, ende, step) step: nur jedes 2. Element ausgeben
    print(count)
    







