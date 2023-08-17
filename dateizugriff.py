import sys

# Dateipfade
# -> Adresse, wo die Datei wohnt
# -> Wegbeschreibung zur Datei
#
# C:\Dokumente\ordner\datei.txt   -> absoluter Pfad (ausgehend vom Ursprung)
#              ordner\datei.txt   -> relativer Pfad (ausgehend vom aktuellen Ort im Dateisystem)


def readfile():
    # Verknüpfung zum Stream herstellen (Datei öffnen)
    try:
        file = open("textdatei.txt", "r")

        # Datei bearbeiten (lesen)
        text = file.read()
        print(text)

        # Stream schliessen (Datei schliessen)
        file.close()
        # print("Am Ende des try-Blocks")
    except IOError:
        print("Die Datei kann nicht geöffnet werden.")

    # print("Zusätzlicher Code irgendwo im Programm")


def writefile():
    # Verknüpfung zum Stream herstellen (Datei öffnen)
    try:
        text = input("Text, der in die Datei geschrieben werden soll:\n")
        file = open("textdatei.txt", "a")

        # Datei bearbeiten (lesen)
        file.write(text)

        # Stream schliessen (Datei schliessen)
        file.close()
        # print("Am Ende des try-Blocks")
    except IOError:
        print("Die Datei kann nicht geöffnet werden.")


readfile()
writefile()
readfile()



# # Exception:

# try:
#     # Code der auszuführen versucht wird
# except FileNotFoundError:
#     # Falls Code nicht ausgeführt werden kann, tue dies hier
# except IOError:
#     # Falls Code nicht ausgeführt werden kann, tue dies hier
# else:
#     # Code der ausgeführt wird, wenn es zu keiner Exception kam
# finally:
#     # Code, der immer ausgeführt wird, egal ob Exception oder nicht