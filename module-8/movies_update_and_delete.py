import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Daniel12!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    cursor.execute("\
                SELECT film_name AS Name,\
                   film_director AS Director,\
                   g.genre_name AS Genre,\
                   s.studio_name AS Studio\
                FROM film f\
                JOIN genre g ON f.genre_id = g.genre_id\
                JOIN studio s ON f.studio_id = s.studio_id\
                   ")
    records = cursor.fetchall()

    print("-- {} --".format(title))

    for film in records:
        print("Film Name: {}\n Director: {}\n Genre Name: {}\n Studio Name: {}\n".format(film[0], film[1], film[2], film[3]))



try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    show_films(cursor, "DISPLAYING FILMS")

    cursor.execute("INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)\
    VALUES('M3GAN', '2022', '102', 'Gerard Johnstone', (SELECT studio_id FROM studio WHERE studio_name = 'Blumhouse Productions'),(SELECT genre_id FROM genre WHERE genre_name = 'Horror') );")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = \"Alien\" ")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE Changed Alien to Horror")

    cursor.execute("DELETE FROM film WHERE film_name = \"Gladiator\" ")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    input("\n\n Press any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exists")
    
    else:
        print(err)
    
finally:
    db.close()