import sys

if __name__ == "__main__":
    arg_list = list(sys.argv)
    del(arg_list[0])
    i = 0
    for arg in arg_list[::-1]:
        if i != 0:
            print("", end=' ')
        i = 1
        for char in arg[::-1]:
            if char.isupper():
                print(char.lower(), end='')
            else:
                print(char.upper(), end='')
    print("")
