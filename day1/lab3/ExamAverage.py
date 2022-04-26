from asyncio.windows_events import NULL


maths_mark = int(input('what was your maths mark? '))
english_mark = int(input('what was your english mark? '))
it_mark = int(input('what was your it mark? '))

avg_mark = (maths_mark + english_mark + it_mark) / 3

grade = NULL

if(avg_mark >= 65):
    grade = 'Pass'
elif(avg_mark < 65):
    grade = 'Fail'
else:
    print('Invalid average mark')


