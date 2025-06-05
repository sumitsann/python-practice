# list allows us to put multiple values in a single varianle
# ordered set of values by index
# index starts from 0

x=[3,5,4,9,7,10]

print(x)

print(x[0])
print(x[4])

# list can contain different value types

y= ['max', 1, 15.5, [3,2]]
print(y[0])
print(y[2])

# length of list
print(len(y))

# inserting value
x.insert(2,'tom')
print(x)

# removing value
x.remove('tom')
print(x)

x.insert(1,3)
print(x)
x.remove(3)
print(x)

# remove last element
print(x.pop())

print(x)

# delete whole list
z=[1,2,4,5,6,3]
del z

# remove all the values from the list (empty the list)
z=[1,2,4,5,6,3]
z.clear()
print(z)

# sorting
x.sort()
print(x)

# reversing the list
x.reverse()
print(x)

# appending
x.append(10)
print(x)

# copying one list to another
s= x.copy()
print(s)

# lets see if we append after copying, does it display
x.append(101)
print(s)


# to check how many number of a specific variables are in the list
print(x.count(10))

















