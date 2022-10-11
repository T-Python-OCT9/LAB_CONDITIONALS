'''
FLOW_CONTROL_CONDITIONALS
'''

## You want to recommend a movie to a friend based on the rating and popularity . To accomplish this do the following : 


# Create a variable for the movie (choose any movie you like)
movie_name : str = "End of The Road"

#Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
movie_rating : int = 3 

# Create a popularity score of type float , let it be 72.65
movie_popularity : float = 72.65

# -------- Using an if statement -----------
# Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if movie_rating >= 4 and movie_popularity > 80 :
    print("Highly recommended")

#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
elif movie_rating >= 3 and movie_popularity > 70 :
    print("I recommended it . It is good")

#else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif movie_rating <= 2 and movie_popularity > 60 : 
    print("You should check it out!")

#else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
elif movie_rating <= 2 and movie_popularity < 50 :
    "Don't watch it. It is a waste of time"