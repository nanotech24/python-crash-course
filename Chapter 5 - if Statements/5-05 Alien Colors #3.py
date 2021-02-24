#Write an if-elif-else chain if alien is green, earn 5 points
#if alien is yellow, 10 points. if alien is red, 15 points.
#Write 3 version of this program and make sure each message is printed 


#print 5 points message
alien_color = 'green'

if alien_color == 'green':
    print('You have earned 5 points!')

elif alien_color =='yellow':
    print('You have earned 10 points!')

else:
    print('You have earned 15 points!')

#Print 10 points message
alien_color = 'yellow'

if alien_color == 'green':
    print('You have earned 5 points!')

elif alien_color == 'yellow':
    print('You have earned 10 points')

else:
    print('you have earned 15 points!')

#Print 15 points message
alien_color = 'red'

if alien_color == 'green':
    print('You have earned 5 points!')

elif alien_color == 'yellow':
    print('You have earned 10 points!')

else:
    print('You have earned 15 points!')