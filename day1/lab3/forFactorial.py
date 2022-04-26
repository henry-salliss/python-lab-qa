user_int = int(input('please enter a number: '))

num = 1

for x in range(1, user_int):
    num *= user_int
    user_int -= 1

print(num)