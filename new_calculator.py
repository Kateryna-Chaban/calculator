import sys

# Display professional application header and operational instructions
print("==================================================")
print("   CLI AUTOMATED CALCULATOR SYSTEM v1.0")
print("==================================================")
print("Supported operations: Addition, Subtraction, Multiplication, Division.")
print("Feature: Memory retention allows utilizing the previous result.")
print("System command: Type 'exit' at any prompt to terminate the program.")
print("==================================================")
print()

# Initialize control and memory variables for the execution cycle
result = None
first_number = ""
second_number = ""
operator = ""

# Execute main processing loop controlled by the termination keyword
while first_number != "exit" and second_number != "exit" and operator != "exit":
    
    # Check if the previous calculation result should be retained as the prime input
    if first_number == result:
        print()
        print(f"Retained first number from memory: {first_number}")

    # Reset and request a new prime input if memory retention is not active
    elif first_number != result:
        first_number = ""
        
        # Internal loop to enforce robust first number data validation
        while first_number == "":
            print()
            try:
                first_number = input("Enter the first number: ").strip().lower()
                
                # Intercept termination request
                if first_number == "exit":
                    break
                    
                # Cast validated string sequence to floating-point numeral
                first_number = float(first_number)
                
            except ValueError:
                # Handle common localized decimal separator delimiter error
                if "," in str(first_number):
                    print("[Syntax Error]: Found ',' instead of '.' as a decimal separator.")
                    print("Please format numbers using a dot character (e.g., 10.5).")
                    first_number = ""
                else:
                    print("[Type Error]: Invalid numeric input detected. Please retry.")
                    first_number = ""

    # Reset and request operator sequence
    operator = ""
    
    # Process operator phase only if termination sequence was not triggered
    if first_number != "exit":
        
        # Internal loop to enforce strict operator compliance
        while operator == "":
            valid_operators = ["+", "-", "*", "/"]
            print()
            operator = input("Enter the mathematical operator (+, -, *, /): ").strip().lower()
            
            # Intercept termination request or validate symbol presence
            if operator == "exit":
                break
            elif operator not in valid_operators:
                print("[Validation Error]: Unsupported arithmetic operator symbol.")
                operator = ""

    # Process secondary numeric input phase if system remains active
    if (first_number != "exit") and (operator != "exit"):
        second_number = ""
        
        # Internal loop to enforce robust second number data validation
        while second_number == "":
            print()
            try:
                second_number = input("Enter the second number: ").strip().lower()
                
                # Intercept termination request
                if second_number == "exit":
                    break
                # Prevent critical division by zero operations runtime failure
                elif (second_number == "0" or second_number == "0.0") and (operator == "/"):
                    print("[Mathematical Error]: Zero division detected. Operation undefined.")
                    second_number = ""
                    continue
                    
                # Cast validated string sequence to floating-point numeral
                second_number = float(second_number)
                
            except ValueError:
                # Handle common localized decimal separator delimiter error
                if "," in str(second_number):
                    print("[Syntax Error]: Found ',' instead of '.' as a decimal separator.")
                    print("Please format numbers using a dot character (e.g., 10.5).")
                    second_number = ""
                else:
                    print("[Type Error]: Invalid numeric input detected. Please retry.")
                    second_number = ""

    # Execute arithmetic computation sequence via match-case statement mapping
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
        # Prompt user for state retention configuration
        print(f"Would you like to preserve {result} as the base for your next calculation?")
        user_response = input("Enter Choice (yes/no): ").strip().lower()
        
        # Evaluate workflow direction or intercept direct close sequence
        if user_response == "yes" or user_response == "y":
            first_number = result
        elif user_response == "exit":
            break

# Display corporate telemetry termination log
print()
print("==================================================")
print("Session terminated. Thank you for using CLI Tools!")
print("==================================================")