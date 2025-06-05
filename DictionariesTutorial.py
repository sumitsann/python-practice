
# list or a map
# list of pairs

D={'name': 'max', 'age':14, 'year':2004}
print(D)

print(D['name'])

# dictionaries can hold multiple data types
E={'name':'Tom', 15:15, 15.1:15.1, True:True, (2,3):5}
print(E[(2,3)])

# length of items in a dictionary
print(len(E))

print(D.get('name'))

# adding element to a dictionary

D['Surname'] = 'Tesar'

print(D)

# removing
D.pop('Surname')
print(D)

E.clear()
print(E)

# deleting a dictionary
del(E)

# changing values

D['name'] = 'tom'

print(D)

# update
D.update({'name':'max'})
print(D)

print(D.keys())
print(D.values())
print(D.items())

# remove last key value pair

D.popitem()

print(D)






















