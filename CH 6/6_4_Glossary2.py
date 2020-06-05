print()
print("Here are some coding word definitions.")
glossary = {
    'variable': 'A container that holds a value.',
    'float': 'A number that contains a decimal point.',
    'string': 'A series of characters.',
    'list': 'A collection of values, each in quotes, in a particular order, separated by a comma, with the collection enclosed by square brackets.',
    'tuple': 'A tuple is the same as a list except the collection is enclosed by parenthesis.',
    'dictionary': 'A collection of key-value pairs.',
    'method': 'An action Python can perform on a piece of data.',
    'concatentation': 'The process of combining strings.',
    'index': 'The position of an item.',
    'looping': 'Taking the same action, or set of actions, on every item in a list.',
}
for k, v in glossary.items():
    print("\n" + k.title() + ": " + v)
print()