#C7-02 P.121 Write a program that asks for dinner group size
#if the answer > 8, print that there is a wait. otherwise the table is ready.


table_size = int(input('How many will be eating today?: '))

if table_size >= 8:
    print('Sorry, there will be a wait.')

else:
    print('Your table is ready!')