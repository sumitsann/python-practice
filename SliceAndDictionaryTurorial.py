a=[0,1,2,3,4,5,6,7,8,9]
b=(0,1,2,3,4,5,6,7,8,9)
c='0123456789'

x=slice(0,5)

print(a[x])

print(a[0:5])

print(b[:6])

print(c[:])

print(c[0:5])

# step values
print(a[0:9:2])
# every third value
print(a[0:9:3])

# negative numbered index
print(c[-1])
print(c[-2])
print(c[-3])

print(a[::-1])
print(a[-3:-1])
print(a[-3::-1])