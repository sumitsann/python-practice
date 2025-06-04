# variable definition

myInt =9
print(myInt)
# variables are case sensitive

myFloat = 20.5
myComplex = 1j

myNum = 10e10
print(myNum)

myString = "Max"
print(myString)
#reassignment of value
myString = 'Tom'
print(myString)

myFloat = myInt
print(myFloat)

#typecasting
myFloat = float(myInt)
print(myFloat)

myInt = int(myFloat)
print(myInt)

# checking the type
print(type(myInt))

print(type(myFloat))
print(type(myNum))
print(type(myString))

#operaror
print(myInt+myFloat)