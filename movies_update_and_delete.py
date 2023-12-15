import mysql.connector

# Connect to MySQL database
movies = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ickes2310",
    database="movies"
)

# Create a cursor object to interact with the database
cursor = mydb.cursor()

# Query 1: Select all fields from the studio table
query1 = "SELECT * FROM studio"
cursor.execute(query1)
result1 = cursor.fetchall()

print("---DISPLAYING Studio RECORDS---")
for row in result1:
    print("Studio ID:", row[0])
    print("Studio Name:", row[1])
    print()

# Query 2: Select all fields from the genre table
query2 = "SELECT * FROM genre"
cursor.execute(query2)
result2 = cursor.fetchall()

print("---DISPLAYING Genre RECORDS---")
for row in result2:
    print("Genre ID:", row[0])
    print("Genre Name:", row[1])
    print()

query3 = "SELECT film_runtime, film_director FROM film"
cursor.execute(query3)
result3 = cursor.fetchall()

print("---DISPLAYING Short Film RECORDS---")
for row in result3:
    print("Film Name:", row[0])
    print("Film Runtime:", row[1])
    print()

query4 = "SELECT film_name, film_director, genre_id, studio_id FROM film ORDER BY film_director"
cursor.execute(query4)
result4 = cursor.fetchall()

print("---DISPLAYING Director RECORDS in Order---")
for row in result4:
    print("Film Name:", row[0])
    print("Film Director:", row[1])
    print()

# Close the cursor and database connection
cursor.close()
mydb.close()


def show_film(cursor, title, films=None):
    cursor.execute(
        "SELECT film_name as NAME, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from "
        "film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    film = cursor.fetchall()
    print(title)
    for film in films:
        print(
            "Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: ()\n".format(film[0], film[1], film[2],
                                                                                       film[3]))


insert_query = ("INSERT INTO film (film_name, film_director, genre_id, studio_id) VALUES ('Gladiator', "
                "'Riley Scott', 'Drama', 'Universal Pictures')")
cursor.execute(insert_query)
mydb.commit()

update_query = "UPDATE film SET genre_id = 'Horror' WHERE film_name = 'Alien'"
cursor.execute(update_query)
mydb.commit()


def show_films(cursor, param):
    pass


show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

delete_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
cursor.execute(delete_query)
mydb.commit()

show_film(cursor, "DISPLAYING FILMS AFTER DELETE")

cursor = mydb.cursor()
