#imagine an alien was shot down. Create a variable called alien_color
#and assign it a value of green, yellow or red. write an if statement to test 
#if the color is green. if so give 5 points. write another that fails

alien_color = 'green'

points = 0

if alien_color == 'green':
    print('You got 5 points!')
    points += 5
    print('You have a total of ' + str(points) + ' points')
    
if alien_color =='red':
    print('You got 10 points!')