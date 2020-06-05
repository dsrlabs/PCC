print()
# First, using a loop, a sentence about each river is printed.
rivers = {
    'nile': 'egypt',
    'shenandoah': 'north america',
    'amazon': 'south america',
}
for k, v in rivers.items():
    print("\n" + "The " + k.title() + " River flows through " + v.title() + ".")
print()
# Next, using a loop, the name of each river (or key) is printed.
print("The name of the rivers are:")
for k in rivers:
    print("\n" + k.title())
print()
print("The name of the countries, in which the rivers flow, are:")
for v in rivers.values():
    print("\n" + v.title())
print()