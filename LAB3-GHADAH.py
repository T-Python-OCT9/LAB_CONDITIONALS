#lab 3 - flow control conditionals 
movie= 'Hichki'
rating = 3
popularty_score= 72.65

if rating >= 4 and popularty_score > 80 :
    print("Highly recommended")
elif rating >=3 and popularty_score > 70 :
    print ("I recommended it . it is good")
elif rating <=2 and popularty_score > 60 :
    print("you should check it out ")
else :
    print("Do'not watch it . it is a waste of time")
