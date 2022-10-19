Movie_Name = "mr.Ahmad"
Rate : int = 3
Popularity :float = 72.65

if Rate >= 4 and Popularity > 80:
    print ("Highly recommended")
elif Rate >= 3 and Popularity > 70:
    print("I recommended it . It is good")
elif Rate <= 2 and Popularity > 60:
    print ("You should check it out!")
elif Rate == 2 and Popularity < 50:
    print("Don't watch it. It is a waste of time")
