while True:
    try:
        #Get numbers and operation
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        #Check and calculate
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by zero.\n")
                continue
            result = num1 / num2
        else:
            print("Invalid operation.\n")
            continue

        #Show result
        print("Result:", result, "\n")

    except ValueError:
        #If input is not a number
        print("Please enter valid numbers.\n")
        continue

    #Ask to continue
    again = input("Do you want to try again? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break
    print()
# End of Calculator.py
