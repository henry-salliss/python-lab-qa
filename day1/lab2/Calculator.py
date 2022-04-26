num1 = int(input('first number: '))
num2 = int(input('second number: '))

operation = input('which operation do you want to peform? + - / * ** : ')


if(operation == '+'):
    print(num1 + num2)
elif(operation == '-'):
    print(num1 - num2)
elif(operation == '/'):
    print(num1 / num2)
elif(operation == '*'):
    print(num1 * num2)
elif(operation == '**'):
    sq_num = int(input(f'which number do you want to square, {num1}? or {num2}? '))
    if(sq_num == num1):
        print(num1 * num1)
    elif(sq_num == num2):
        print(num2 * num2)
    else:
        print(f'please enter either {num1} or {num2}')
else:
    print('please enter a valid operation')