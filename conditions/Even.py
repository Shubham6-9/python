def main():
    number = input("Enter number : ")
    if is_even(int(number)):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
