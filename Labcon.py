movie_name : str = "Theking" 
rate_the_movie : int = 3
popularity : float = 72.65

if rate_the_movie >= 4 and popularity > 80 :
     print("Highly recommended")
elif rate_the_movie >= 3 and popularity > 70 :
     print("I recommended it . It is good") 
elif rate_the_movie <= 2 and popularity > 60 :
     print("You should check it out!") 
elif rate_the_movie <= 2 and popularity < 50 :
     print("Don't watch it. It is a waste of time") 
else :
     print("nothing") 

     


