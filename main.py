MovieName :str = "The forgotten"
Rateing :int = 3
popularity :float = 72.65

#if statement Start Here
if Rateing >= 4 and popularity >80:
    print("Highly recommended")
elif Rateing >= 3 and popularity >70:
     print("I recommended it . It is good")
elif Rateing <= 2 and popularity >60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
