f = open ("input.txt", "r")
lines = f.readlines()
max = 0
tmp = 0

for i in lines:
    if i != '\n':
        tmp += int(i)
    else :
        if tmp > max :
            max = tmp
        tmp = 0

print(max)                        