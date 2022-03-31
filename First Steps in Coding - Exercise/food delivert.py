chicken_menu = int(input())
fish_menu = int(input())
vegeterian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegeterian_price = vegeterian_menu * 8.15
delivery_price = 2.50

menu_total = chicken_price + fish_price + vegeterian_price
dessert_price = menu_total * 0.2

total_sum = menu_total + dessert_price + delivery_price
print(total_sum)