def calculate():
    try:
        
        num1 = float(input("Enter the first number: "))
        
        num2 = float(input("Enter the second number: "))
        
      
        operation = input("Enter an operation (+, -, *, /): ")

        result = None
    
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero.")
                
                return
        else:
            
            print("Error: Invalid operation. Please use +, -, *, or /.")
        
            return
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        
        print("Error: Invalid input. Please enter valid numbers.")
calculate()
