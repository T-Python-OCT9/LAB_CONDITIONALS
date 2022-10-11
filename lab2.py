Movie = 'The Hallowen'

the_rate = 3
popularity_score = 72.65

if the_rate >= 4:
    print('Highly recommended')
    
elif the_rate >=3 :
    print('I recommended it . It is good')

elif the_rate <=2 :
    print('You should check it out!')

elif the_rate <=2 and popularity_score < 50 :
    print('Dont watch it. It is a waste of time')

else: print('go to bed')

