f = open ("input.txt", "r")
lines = f.readlines()
max = 0
maxThree = []
tmp = 0
sum = 0

for i in lines:
    if i != '\n':
        tmp += int(i)
    else : 
        maxThree.append(tmp)    
        tmp = 0
maxThree.sort()

for i in range(-3,0):
    sum += maxThree[i]
 
print(sum)