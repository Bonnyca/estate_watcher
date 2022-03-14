def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    return n


def main():
    n = 10
    n = divide_and_round(n)
    print(n)

main()