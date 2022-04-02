jury = int(input())
total_grade = 0
presentation_count = 0
total_average_grade = 0
presentation = str(input())
while presentation != "Finish":
    total_grade = 0
    presentation_count += 1
    for i in range(jury):
        grade = float(input())
        total_grade += grade
    average_grade = total_grade / jury
    print(f"{presentation} - {average_grade:.2f}.")
    total_average_grade += average_grade
    presentation = str(input())
total_average_grade = total_average_grade / presentation_count
print(f"Student's final assessment is {total_average_grade:.2f}.")