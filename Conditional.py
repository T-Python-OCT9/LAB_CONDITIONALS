name_movie : str = "God father"
rating_movie : int = 3
popularity_score : float = 72.65



if rating_movie >= 4 and popularity_score > 80:
    print("Highly recommended")

elif rating_movie >= 3 and popularity_score > 70:
    print("I recommended it . It is good")
elif rating_movie <= 2 and popularity_score > 60:
    print("You should check it out!")
else:
    ("Don't watch it. It is a waste of time")

