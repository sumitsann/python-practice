
# in curly brackets
# cannot have duplicate values

A={1,2,5,4,7,9,2}
print(A)

# duplicate values are removed
# always have unique values

# methods in sets

print(len(A))

A.add(10)
print(A)

# adding multiple values in a set
A.update([15,18,17,14])
print(A)

# remove
A.remove(18)
print(A)

# discard also removes

A.discard(17)
print(A)

# discard does not throw error but remove does

# remove any random element from a set
A.pop()
print(A)

name={'max', 'tom', 'Den'}
name.clear()
print(name)

del name

# assigning set in square bracket

Z=set([1,2,3,5])
print(Z)

B={10,11,12,13,14,16,18}

# or
print(A|B)

# union
print(A.union(B))

# intersection common elements between two sets
print(A&B)

print(A.intersection(B))

# difference of two sets

print(A-B)

print(B-A)

print(A.difference(B))
print(B.difference(A))

# symmetric difference in two sets

print(A^B)
print(B^A)
print(A.symmetric_difference(B))


# sets are not ordered or indexed
# unordered

# to know all the methods in the set
print(dir(A))

