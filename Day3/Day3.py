#priorities:
#a-z : 1-26
#   ord(x) - ord ('a') + 1
#A-Z : 27-52
#   ord (x) - ord ('A') + 27

def main():
    f = open("input.txt", "r")
    x = f.readlines()

    


if __name__ == "__main__":
    t = main()
    x = 0
    for i in t:
        x += i
    print(x)    