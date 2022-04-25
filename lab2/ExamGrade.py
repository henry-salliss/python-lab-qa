exam_mark = int(input('what mark did you get on your exam (between 1-100) ? '))

if(exam_mark < 1 or exam_mark > 100):
    print('error, mark has to be between 1 and 100')
elif(exam_mark < 50):
    print('you failed son')
elif(exam_mark >=50 and exam_mark <=60):
    print('you passed!')
elif(exam_mark > 60 and exam_mark <=70):
    print('you got a merit')
elif(exam_mark > 70 and exam_mark <= 100):
    print('you got a distinction 🥳')