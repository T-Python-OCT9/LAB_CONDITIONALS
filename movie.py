movie1 : str = "movie 1"
rating : int = 5
ratingmovie1 : int = 3
popularity : float = 72.65


if ratingmovie1 >= 4 and popularity > 80 :
    print("Highly recommended")
elif ratingmovie1 >=3 and popularity > 70 :
    print("I recommended it . It is good")
elif ratingmovie1 <=2 and popularity > 60 :
    print("You should check it out!")
elif ratingmovie1 <=2 and popularity < 50:
    print("Don't watch it. It is a waste of time")

