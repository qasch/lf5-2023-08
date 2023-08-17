import sqlite3

def display_movies():
    try:
        # Verbindung zur Datenbank herstellen
        connection = sqlite3.connect("../dbs/custom/filme.db")

        # Cursor Objekt erzeugen
        cursor = connection.cursor()

        # SQL ausführen
        sql_statement = "SELECT * FROM film;"
        cursor.execute(sql_statement)

        print("Es gibt folgende Filme in unserer Datenbank: ")
        for line in cursor:
            print(line[1])

    except Exception as e:
        print("Folgender Fehler ist aufgetreten: " + e.args[0])
    finally:
        # Verbindung zur Datenbank schliessen
        connection.close()

def insert_movies():
    try:
        # Verbindung zur Datenbank herstellen
        connection = sqlite3.connect("../dbs/custom/filme.db")

        # Cursor Objekt erzeugen
        cursor = connection.cursor()

        # SQL ausführen
        sql_statement = "INSERT INTO film (name, erscheinungsjahr, genre) VALUES ('Oppenheimer', '2023', 'Doku');"
        cursor.execute(sql_statement)

        # INSERT Statement wirklich durchführen
        connection.commit()

    except Exception as e:
        print("Folgender Fehler ist aufgetreten: " + e.args[0])
    finally:
        # Verbindung zur Datenbank schliessen
        connection.close()


display_movies()
insert_movies()
display_movies()

