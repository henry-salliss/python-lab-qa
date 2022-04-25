exam_mark = int(input('what was your exam mark? '))
student_level = int(input('what level student are you, 1 or 2? '))

if(student_level == 1):
    if(exam_mark < 1 or exam_mark > 100):
        print('error, mark cannot be more than 100 or less than 1')
    elif(exam_mark < 50):
        print('you failed son')
    elif(exam_mark >=50 and exam_mark <=60):
        print('you passed!')
    elif(exam_mark > 60 and exam_mark <=70):
        print('you got a merit')
    elif(exam_mark > 70 and exam_mark <= 100):
        print('you got a distinction 🥳')
elif(student_level == 2):
    if(exam_mark < 1 or exam_mark > 100):
        print('error, mark cannot be more than 100 or less than 1')
    elif(exam_mark < 40):
        print('you failed son')
    elif(exam_mark >=40 and exam_mark <=50):
        print('you passed!')
    elif(exam_mark > 50 and exam_mark <=65):
        print('you got a merit')
    elif(exam_mark > 65 and exam_mark <= 100):
        print('you got a distinction 🥳')