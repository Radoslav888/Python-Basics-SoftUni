count_grades = int(input())
poor_grade = 0
grade_sum = 0
grades = 0
last_problem = "a"
fail = False
while True:
    problem_name = str(input())
    if problem_name == "Enough":
        break
    grade = int(input())
    grade_sum += grade
    grades += 1
    last_problem = problem_name
    if grade <= 4:
        poor_grade += 1
    if poor_grade >= count_grades:
        print(f"You need a break, {poor_grade} poor grades.")
        fail = True
        break


if not fail:
        grade_average = grade_sum / grades
        print(f"Average score: {grade_average:.2f}")
        print(f"Number of problems: {grades}")
        print(f"Last problem: {last_problem}")