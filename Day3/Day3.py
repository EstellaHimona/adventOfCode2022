#priorities:
#a-z : 1-26
#   ord(x) - ord ('a') + 1
#A-Z : 27-52
#   ord (x) - ord ('A') + 27

# def main():
from curses.ascii import isupper


f = open("input.txt", "r")
x = f.readlines()
sum = 0

for j in x:
    firstHalf = j[:len(j)//2]
    secondHalf = j[len(j)//2:]
    
    for y in firstHalf:
        if y in secondHalf:
            break

    if isupper(y):
        sum += ord(y) - ord('A') + 27
    else:
        sum += ord(y) - ord('a') + 1
print(sum)


# if __name__ == "__main__":
#     t = main()
#     x = 0
#     for i in t:
#         x += i
#     print(x)    