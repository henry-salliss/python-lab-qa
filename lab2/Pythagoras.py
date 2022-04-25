import math

num = int(input('which side do you want to calculate A (1), B (2), C (3)? '))

if(num == 1):
    b_length = int(input('how long is side B '))
    c_length = int(input('how long is side C '))
    print(f'the length of side A is {math.sqrt(b_length ** 2 + c_length ** 2)}')
elif(num == 2):
    a_length = int(input('how long is side A '))
    c_length = int(input('how long is side C '))
    print(f'the length of side A is {math.sqrt(a_length ** 2 + c_length ** 2)}')
elif(num == 3):
    a_length = int(input('how long is side A '))
    b_length = int(input('how long is side B '))
    print(f'the length of side A is {math.sqrt(a_length ** 2 + b_length ** 2)}')