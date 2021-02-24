#6-03 p.102 think of five programming words, add them to a dict wuth meanings

glossary = {
    'variable' : 'Holds a value associated with the varaible name.',
    'string' : 'A string is simply a series of characters.',
    'float' : 'Python calls any number with a decimal point a float.',
    'comment' : 'In python, the hash mark (#) indicates a code comment.',
    'list' : 'A list is a collection of items in a particular order.'
    }

print(
    'Variable: ' + glossary['variable'] +
    '\n\nString: ' + glossary['string'] + 
    '\n\nFloat: ' + glossary['float'] +
    '\n\nComment: ' + glossary['comment'] + 
    '\n\nList: ' + glossary['list']
    )