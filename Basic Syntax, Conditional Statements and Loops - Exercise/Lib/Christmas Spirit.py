quantity = int(input())
days = int(input())
chrismast_spirit = 0
total_cost = 0
condition_5th_day = False

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for i in range(1, days + 1):
    condition_5th_day = False
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        chrismast_spirit += 5
        total_cost += ornament_set * quantity
    if i % 3 == 0:
        chrismast_spirit += 13
        total_cost += (tree_skirt * quantity) + (tree_garlands * quantity)
        condition_5th_day = True
    if i % 5 == 0:
        chrismast_spirit += 17
        total_cost += quantity * tree_lights
        if condition_5th_day == True:
            chrismast_spirit += 30
    if i % 10 == 0:
        chrismast_spirit -= 20
        total_cost += 23

        if i == days:
            chrismast_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {chrismast_spirit}")


