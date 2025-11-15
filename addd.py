try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    addition = a + b
    subtraction = a - b

    print("Addition:", addition)
    print("Subtraction:", subtraction)

except ValueError:
    print("Error: Please enter only numbers!")
