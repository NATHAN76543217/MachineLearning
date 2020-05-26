import sys


if __name__ == "__main__":
    nb_arg = len(sys.argv)
    if nb_arg != 3:
        if nb_arg > 3:
            print("InputError: too many arguments\n")
        elif nb_arg == 2:
            print("InputError: not enought arguments\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
        exit()
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except ValueError:
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:\n\tpython operations.py 10 3")
        exit()
    res_add = nb1 + nb2
    res_sub = nb1 - nb2
    res_mult = nb1 * nb2
    try:
        res_div = nb1 / nb2
    except ZeroDivisionError:
        res_div = "ERROR (div by zero)"
    try:
        res_rem = nb1 % nb2
    except ZeroDivisionError:
        res_rem = "ERROR (modulo by zero)"
    print("Sum:\t\t", res_add)
    print("Difference:\t", res_sub)
    print("Product:\t", res_mult)
    print("Quotient:\t", res_div)
    print("Remainder:\t", res_rem)
