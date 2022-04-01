money_needed = float(input())
money = float(input())
days_spending = 0
days = 0
enough = 0
while True:
    spend_or_save = str(input())
    days += 1
    how_much = float(input())
    if spend_or_save == "save":
        days_spending == 0
    if spend_or_save == "spend":
        days_spending += 1
        if days_spending >= 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break

    if spend_or_save == 'spend':
        money -= how_much
        if money < 0:
            money = 0
    elif spend_or_save == 'save':
        money += how_much
    if money >= money_needed:
        enough = True
        break
if enough:
    print(f"You saved the money for {days} days.")
