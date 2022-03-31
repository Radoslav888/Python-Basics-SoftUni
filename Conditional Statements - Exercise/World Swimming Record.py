record = float(input())
meters = float(input())
time_for_1_m = float(input())

seconds = meters * time_for_1_m

delay = meters // 15 * 12.5
time_with_delay = seconds + delay


if time_with_delay < record:
    print(f"Yes, he succeeded! The new world record is {time_with_delay:.2f} seconds.")

else:
    difference = time_with_delay - record
    print(f"No, he failed! He was {difference:.2f} seconds slower.")