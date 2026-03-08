x = float(input("Enter number 1: ").strip())
sign = input("enter sign(+, -, x, /, %): ")
y = float(input("Enter number 2: ").strip())

match sign:
    case '+':
        print(f"Ans : {x+y}")
    case '-':
        print(f"Ans : {x-y}")
    case 'x':
        print(f"Ans : {x*y}")
    case '/':
        if(y==0):
            print("Error!")
        else:
            print(f"Ans : {round(x/y, 2)} / {(x/y):.2f}")
    case '%':
        print(f"Ans : {x%y}")
    case _:
        print("Enter proper sign.")