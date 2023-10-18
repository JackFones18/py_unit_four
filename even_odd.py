
def even_or_odd(number):
    """
    Create a function that will tell if a number is even or odd. Use two if statements to do this.
    :param number: could be any positive or negative integer
    :return: either "x is an even number" or "x is an odd number"
    """
    if number%2==0:
        return("number is even")
    else:
        return("number is odd")


def main():
    thingy = float(input("number: "))
    print(even_or_odd(thingy))



if __name__ == '__main__':
    main()