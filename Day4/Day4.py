#In how many assignment pairs does one range fully contain the other? 

f = open("input.txt", "r")
lines = f.readlines()
sum = 0

for i in lines :
    x, y = i.split(',')
    x1 = x.split ('-')
    y1 = y.split ('-')

    if (int(x1[0]) <= int(y1[0]) and int(x1[1]) >= int(y1[1])) or (int(y1[0]) <= int(x1[0]) and int(y1[1]) >= int(x1[1])) :
        sum += 1

print(sum)    

