user_int = int(input('please enter a number: '))

num = 1

while user_int >= 1:
    num *= user_int
    user_int -= 1

print(num)