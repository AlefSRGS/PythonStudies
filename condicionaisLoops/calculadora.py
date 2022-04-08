num1 = int(input())
num2 = int(input())
operation = input('')
result = 0

if operation == '+':
    result = num1 + num2
    print(f"{result:.3f}")
elif operation == '-':
    result = num1 - num2
    print(f"{result:.3f}")
elif operation == '/':
    if num2 == 0:
        print('operation cannot being complete')
    else: 
        result = num1 / num2
        print(f"{result:.3f}")
elif operation == '*':
    result = num1 * num2
    print(f"{result:.3f}")

while operation != '&':
    num2 = int(input())
    operation = input()

    if operation == '+':
        result = result + num2
        print(f"{result:.3f}")
    elif operation == '-':
        result = result - num2
        print(f"{result:.3f}")
    elif operation == '/':
        if num2 == 0:
            print('operation cannot being complete')
        else: 
            result = result / num2
            print(f"{result:.3f}")
    elif operation == '*':
        result = result * num2
        print(f"{result:.3f}")