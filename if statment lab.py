movie_name ="catch me if you can"
movie_rate :int =3
movie_score :float =72.65

if movie_rate>=4 and movie_score >= 80:
    print("Highly recommended")
elif movie_rate>=3 and movie_score >= 70:
    print("I recommended it . It is good")
elif movie_rate<=2 and movie_score >= 60:
    print("You should check it out!")
elif movie_rate<=2 and movie_score <= 50:
    print("Don't watch it. It is a waste of time")