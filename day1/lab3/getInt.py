user_int = int(input('please input a number between 1 and 100: '))
min_value = 1
max_value = 100
count = 1

while(count < 3):
    if(user_int >= min_value and user_int <= max_value):
        print(f'your number was {user_int}')
        break
    else:
       user_int = int(input('please input a number between 1 and 100: '))
       count += 1

if(count >= 3):
    print(user_int or 'did not enter valid number')