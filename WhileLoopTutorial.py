
#  allows to repeat over some block of code until the condition is met

i=0
while i<5:
    print("the value of i is : ", i)
    i+=1
print("Finished with loop")

num = 1
sum = 0

print("Enter a number. Please enter 0 to Exit")

while num != 0:
    num = float(input("Number? "))
    sum=sum+num
    print("sum= ", sum)
else:
    print("Finished Sum")