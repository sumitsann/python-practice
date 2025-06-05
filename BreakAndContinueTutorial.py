
a=[0,1,2,3,4,5]

for x in a:
    if x==2:
        break
    print(x)

print('----------------------------------------------')
i=0
while i<5:
    i+=1
    if i==4:
        continue
    print(i)
    i+=1

# continue : skip the passing condition
# break: break the loop when passing the condition

