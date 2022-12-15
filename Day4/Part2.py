#In how many assignment pairs do the ranges overlap?

f = open("input.txt", "r")
lines = f.readlines()
sum = 0

for i in lines :
    x, y = i.split(',')
    x1 = x.split ('-')
    y1 = y.split ('-')

    if int(x1[0]) <= int(y1[1]) and int(x1[1]) >= int(y1[0]):
        sum += 1

print(sum)  