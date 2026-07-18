# Display program instructions
print("--- Calculator Program ---")
print("Operations: Add (+), Subtract (-), Multiply (*), Divide (/)")
print("Features: You can use the previous result as the first number.")
print("System command: Type 'exit' at any prompt to stop the program.")
print()

# Initialize variables
result = None
first_number = ""
second_number = ""
operator = ""

# Main program loop
while first_number != "exit" and second_number != "exit" and operator != "exit":
    
    # Check if the previous result should be used
    if first_number == result:
        print()
        print(f"First number (from memory): {first_number}")

    # Request a new first number
    elif first_number != result:
        first_number = ""
        
        while first_number == "":
            print()
            try:
                first_number = input("Enter the first number: ").strip().lower()
                
                if first_number == "exit":
                    break
                    
                first_number = float(first_number)
                
            except ValueError:
                if "," in str(first_number):
                    print("Error: Please use '.' instead of ',' for decimals.")
                    first_number = ""
                else:
                    print("Error: Invalid number. Please try again.")
                    first_number = ""

    # Request operator phase
    operator = ""
    if first_number != "exit":
        while operator == "":
            valid_operators = ["+", "-", "*", "/"]
            print()
            operator = input("Enter the operator (+, -, *, /): ").strip().lower()
            
            if operator == "exit":
                break
            elif operator not in valid_operators:
                print("Error: Unsupported operator. Please try again.")
                operator = ""

    # Request second number phase
    if (first_number != "exit") and (operator != "exit"):
        second_number = ""
        
        while second_number == "":
            print()
            try:
                second_number = input("Enter the second number: ").strip().lower()
                
                if second_number == "exit":
                    break
                elif (second_number == "0" or second_number == "0.0") and (operator == "/"):
                    print("Error: Division by zero is not allowed.")
                    second_number = ""
                    continue
                    
                second_number = float(second_number)
                
            except ValueError:
                if "," in str(second_number):
                    print("Error: Please use '.' instead of ',' for decimals.")
                    second_number = ""
                else:
                    print("Error: Invalid number. Please try again.")
                    second_number = ""

    # Calculation phase
    if (first_number != "exit") and (operator != "exit") and (second_number != "exit"):
        match operator:
            case "+":
                result = first_number + second_number
                print(f"Result: {first_number} + {second_number} = {result}")
            case "-":
                result = first_number - second_number
                print(f"Result: {first_number} - {second_number} = {result}")
            case "*":
                result = first_number * second_number
                print(f"Result: {first_number} * {second_number} = {result}")
            case "/":
                result = first_number / second_number
                print(f"Result: {first_number} / {second_number} = {result}")

        print()
        # Memory configuration prompt
        print(f"Do you want to use {result} for the next calculation?")
        user_response = input("Answer (yes/no): ").strip().lower()
        
        if user_response == "yes" or user_response == "y":
            first_number = result
        elif user_response == "exit":
            break

print()
print("Program terminated. Goodbye!")