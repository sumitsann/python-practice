
# Tuples are immutable
# once they are created they cannot be changed
# instead of square brackets using parenthesis ()
x= (1,5,3,4,8)

print(x)

print(x[0])
print(x[4])

# x[0] = 2
#
# print(x)

# we cannot use functions like append, remove, change elements
print(x.count(8))

print(len(x))

# tuples can hold multiple data types
y=(1, 'max', 1.6)
print(y)

# concatinating two tuples
z=x+y
print(z)


a=('hi',)* 5
print(a)


# max min and delete
print(max(x))
print(min(x))
del(z)



