needed_nylon = int(input())
needed_paint = int(input())
quantity_thinner = int(input())
hours = int(input())

nylon_price = (needed_nylon + 2) * 1.50
paint_price = (needed_paint + needed_paint * 0.1) * 14.50
thinner_price = quantity_thinner * 5.00
bag = 0.4

supplies_sum = nylon_price + paint_price + thinner_price + bag

work_pricing = (supplies_sum * 0.3) * hours

total = supplies_sum + work_pricing

print(total)

