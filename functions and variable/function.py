def main():
    name = input("Enter name : ")
    hello(name)
    hello()
    print(f"{(sq(40.2)):.2f}")


def hello(name="your_name"):
    print(f"Hello {name}")


def sq(num):
    return num * num

main()
