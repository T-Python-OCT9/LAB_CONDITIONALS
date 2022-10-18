name_movie : str = "godfather"

rating_movie : int = 4

ty_score : float = 72.65

if rating_movie >= 4 and ty_score > 80:
 print("Highly recommended")

elif rating_movie >= 3 and ty_score > 70:
 print("I recommended it . It is good")

elif rating_movie <= 2 and ty_score > 60:
 
 print("You should check it out!")
        
else:
 print("Don't watch it. It is a waste of time")
