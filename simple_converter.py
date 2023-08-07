## Alternativen, allerdings weniger flexibel:
#print("3 Tage sind" , int(3 * 24) , "Stunden.")
#print("3 Tage sind" , 3 * 24 , "Stunden.")

anzahl_tage = 18
umrechung_stunden = 24
umrechung_minuten = 24 * 60
umrechung_sekunden = 24 * 60 * 60


print(str(anzahl_tage) + " Tage sind " + str(anzahl_tage * umrechung_stunden) + " Stunden.")
print(str(anzahl_tage) + " Tage sind " + str(anzahl_tage * umrechung_minuten) + " Minuten.")
print(str(anzahl_tage) + " Tage sind " + str(anzahl_tage * umrechung_sekunden) + " Sekunden.")


# 3 ist hier ein Integer, wird vor der Ausgabe von print() automatisch (implizit) in einen String umgewandelt
print("eins", "zwei", 3)     
# 3 ist hier ein String, muss nicht mehr umgewandelt werden
print("eins", "zwei", "3")