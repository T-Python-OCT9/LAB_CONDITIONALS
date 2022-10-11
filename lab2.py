Movie_name : str = "Red"

Movie_rating : int = 3

score_popularity : float = 72.65

if Movie_rating >= 4  and score_popularity >= 80 :
    print("Highly recommended")
elif Movie_rating >= 3 and score_popularity > 70 :  
    print("I recommended it . It is good")
elif Movie_rating <= 2  and score_popularity > 60 :
    print("You should check it out!")
else :
     Movie_rating <= 2 and score_popularity < 50
     print("Don't watch it. It is a waste of time")     
