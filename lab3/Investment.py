initial_investment = int(input('how much do you want to invest? '))
target_value = int(input('how much do you want to make before stopping? '))
interest_rate = float(input('what is the interest rate? '))
years = int(input('how long do you want to invest? '))

while(initial_investment <= target_value):
    initial_investment *= interest_rate
    years += 1

print(f'it will take {years} years for you to hit your target, at which point your investment will have increased to {initial_investment}')