import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Daniel12!",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1]))
    
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()

    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    runtimes = cursor.fetchall()

    print("-- DISPLAYING Short Film RECORDS --")
    for runtime in runtimes:
        print("Film Name: {}\n Runtime: {}\n".format(runtime[0], runtime[1]))

    cursor.execute("SELECT film_name, film_director FROM film GROUP BY film_name, film_director ORDER BY film_director")
    directors = cursor.fetchall()

    print("-- DISPLAYING Director RECORDS in Order --")
    for director in directors:
        print("Film Name: {}\n Director: {}\n".format(director[0], director[1]))

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
