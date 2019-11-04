marvel_movies = ["Iron Man", "The Incredible Hulk", "Thor", "Captain America: The First Avenger", "Marvel's The Avengers", "Thor: The Dark World", "Captain America: The Winter Soldier", "Guardians of the Galaxy", "Avengers: Age of Ultron", "Ant-Man"]
special_marvel_movies = []

for marvel_movies in marvel_movies:
    if "The" in marvel_movies:
        special_marvel_movies.append(marvel_movies)
print(special_marvel_movies)