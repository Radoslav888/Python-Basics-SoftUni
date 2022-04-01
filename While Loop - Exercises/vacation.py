money_needed = float(input())
money = float(input())
days = 0
spending_days = 0

while money < money_needed and spending_days < 5:
    save_or_spend = str(input())
    how_much = float(input())
    days += 1
    if save_or_spend == "save":
        spending_days = 0
        money += how_much
    elif save_or_spend == "spend":
        spending_days += 1
        money -= how_much
        if money < 0:
            money = 0
if spending_days >= 5:
    print(f"You can't save the money.")
    print(f"{days}")
elif money >= money_needed:
    print(f"You saved the money for {days} days.")