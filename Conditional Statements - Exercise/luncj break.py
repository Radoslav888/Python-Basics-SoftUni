import math
serial = str(input())
duration_episode = int(input())
lunch_break_duration = int(input())

lunch_duration = lunch_break_duration * 0.125
chill_time = lunch_break_duration * 0.25
round(lunch_duration)
time_left = lunch_break_duration - lunch_duration - chill_time

time_left_after_watching = abs(time_left - duration_episode)

if time_left_after_watching % 1 == 0.5:
   time_left_after_watching += 0.5



if time_left >= duration_episode:
    print(f"You have enough time to watch {serial} and left with {time_left_after_watching:.0f} minutes free time.")

else:
    print(f"You don't have enough time to watch {serial}, you need {time_left_after_watching:.0f} more minutes.")