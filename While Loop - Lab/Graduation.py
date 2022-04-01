name = str(input())
clas = 0
grade_sum = 0
grade_average = 0
while True:
    grade = float(input())
    clas += 1
    grade_sum += grade
    grade_average = grade_sum / 12
    if grade < 4.00:
        print(f"{name} has been excluded at {clas} grade")
        break
    if clas == 12:
        print(f'{name} graduated. Average grade: {grade_average:.2f}')
        break