#6-04 p.108 use a for loop to print keys and values of dictionary from 
#Excersise 6-03, then add 5 more terms

glossary = {
    'variable' : 'Holds a value associated with the varaible name.',
    'string' : 'A string is simply a series of characters.',
    'float' : 'Python calls any number with a decimal point a float.',
    'comment' : 'In python, the hash mark (#) indicates a code comment.',
    'list' : 'A list is a collection of items in a particular order.',
    'sorted' : 'Sort data numerically or alphabetically, not permanent.',
    'int' : 'integer data type for non decimal numbers.',
    'function' : 'Reusable bit of code that can take arguments.',
    'dictionary' : 'like a list, but holds keys with associated values.',
    'pop' : 'used to "pop" an item from the end of a list.'
    }


#the for loop printing all of the terms and definitions of the glossary
for term, definition in glossary.items():

    print(term.title() + ': ' + definition.title() + '\n')