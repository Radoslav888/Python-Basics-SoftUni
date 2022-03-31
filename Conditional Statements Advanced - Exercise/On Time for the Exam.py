exam_hour = int(input())
exam_minute = int(input())
hour_arrived = int(input())
minute_arrived = int(input())

time_of_exam = exam_hour * 60 + exam_minute
time_of_arriving = hour_arrived * 60 + minute_arrived



if time_of_arriving > time_of_exam:
    print("Late")

elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")

elif time_of_exam - 30 > time_of_arriving:
    print("Early")

difference = abs(time_of_exam - time_of_arriving)

if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{difference} minutes before the start")

elif time_of_arriving <= time_of_exam - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
       print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_exam + 60 > time_of_arriving > time_of_exam:
    print(f"{difference} minutes after the start")

elif time_of_arriving >= time_of_exam + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
       print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
