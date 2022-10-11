'''
This is the 2nd Python lab

'''

movie_name: str = "Interstellar"

movie_rating: int = 3

movie_popularity: float = 72.65


if movie_rating >= 4 and movie_popularity > 80:
    print("Highly recommended")

elif movie_rating >= 3 and movie_popularity > 70:
    print("I recommend it, it is good")

elif movie_rating <= 2 and movie_popularity > 60:
    print("You should check it out!")

else:
    print(" Don't watch it. It is a waste of time")


