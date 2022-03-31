deposit = float(input())
deposit_time = int(input())
annual_interest = float(input())
annual_interest_percent = annual_interest / 100
total = deposit + deposit_time * ((deposit * annual_interest_percent) / 12)
print(total)