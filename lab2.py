my_fav_movie = "hope"
rate = 3
popularity : float = 72.65


if rate >= 4 and popularity > 80:
    print("Highly recommended")
elif rate >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif rate <= 3 and popularity > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")