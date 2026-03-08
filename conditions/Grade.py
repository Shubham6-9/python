mark = float(input("Enter marks : "))

marks = int(mark)
if(marks > 100):
    print("Marks to proper daal.")
elif(marks >= 90):
    print("Grade A")
elif(marks >= 75):
    print("Grade B")
elif(marks >= 55):
    print("Grade C")
elif(marks >= 35):
    print("Grade D")
elif(marks >= 0):
    print("Grade F")
else:
    print("Enter proper marks")