import Movie
import Thriller


if __name__ == '__main__':
    movie = Movie
    thriller = Thriller

    Movie = [("The Khingt of Darkness", 2008), ("Cricket Club", 1999), ("Jockey", 2019),
                ("Leon", 1994), ("Kill Bill", 2003), ("Parasite", 2019), ]
    print(sorted(Movie))


    Movie1 = ("Games of Thrones", 2012)
    print(Movie.append(Movie1))
    print(Movie)
    # print("The new list: ", Movie.get_all_movies())


    print(thriller.get_all_movies(Movie))




