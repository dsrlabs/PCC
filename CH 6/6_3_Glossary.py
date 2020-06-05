print()
glossary = {
    'variable': 'A container that holds a value.',
    'float': 'A number that contains a decimal point.',
    'string': 'A series of characters.',
    'list': 'A collection of values, each in quotes, separated by a comma, with the collection enclosed by square brackets.',
    'tuple': 'A tuple is the same as a list except the collection is enclosed by parenthesis.',
}
print("Variable: " + glossary['variable'])
print("Float: " + glossary['float'])
print("String: " + glossary['string'])
print("List: " + glossary['list'])
print("Tuple: " + glossary['tuple'])
print()

#The above code gives the correct output EXCEPT the newline character was not used to place a space between each
#definition, as instructed in the exercise.  The code below includes the instruction by assign a variable to each
#word, then using the newline character title function on the word. When this is done, the word to be defined
#only has to be typed once, and the items to be printed will be formatted correctly.

word = 'variable'
print("\n" + word.title() + ": " + glossary[word])

word = 'float'
print("\n" + word.title() + ": " + glossary[word])

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'tuple'
print("\n" + word.title() + ": " + glossary[word])