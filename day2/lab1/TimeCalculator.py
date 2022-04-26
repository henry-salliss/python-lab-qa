date = input('please enter a  date in the format dd:hh:mm ')
date_two = input('please enter a another date in the format dd:hh:mm ')

formatted_date_one = date.split(':')
formatted_date_two = date_two.split(':')

print(formatted_date_one, formatted_date_two)

for time in formatted_date_one:
    int(time)

print(formatted_date_one)