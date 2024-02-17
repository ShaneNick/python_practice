def clean_input(input_str):
    # Remove non-numeric characters except the minus sign for negative numbers
    return ''.join(filter(lambda x: x.isdigit() or x == '-', input_str))

while True:
    equation = input('Please type in your mathematical equation or type "exit" to end calculations: ')
    if equation.lower() == 'exit':
        break

    # Identify the operation
    if '+' in equation:
        numbers = equation.split('+')
    elif '-' in equation:
        numbers = equation.split('-')
    elif '*' in equation:
        numbers = equation.split('*')
    elif '/' in equation:
        numbers = equation.split('/')
    else:
        print("Invalid equation. Please try again.")
        continue
    
    try:
        # Clean and convert the numbers before performing operations
        num1 = int(clean_input(numbers[0]))
        num2 = int(clean_input(numbers[1]))
        
        # Perform the operation
        if '+' in equation:
            print(num1 + num2)
        elif '-' in equation:
            print(num1 - num2)
        elif '*' in equation:
            print(num1 * num2)
        elif '/' in equation:
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print(num1 / num2)
    except ValueError:
        print("There was an error with the input. Please ensure you are entering numbers.")
