budget = float(input())
one_kg_flour = float(input())
one_pack_eggs = one_kg_flour * 0.75
one_liter_milk = one_kg_flour * 1.25
quater_liter_milk = one_liter_milk * 0.25
one_loaf = one_kg_flour + one_pack_eggs + quater_liter_milk
loaves = 0
eggs = 0



while True:
    budget_left = budget
    budget -= one_loaf
    if budget <= 0:
        break
    loaves += 1
current_loaves = loaves
for i in range(1, loaves + 1):
    eggs += 3


    if i % 3 == 0:
        eggs_lost = current_loaves - 2
        if eggs_lost > 0:
           eggs -= eggs_lost
    current_loaves -= 1

print( f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget_left:.2f}BGN left.")