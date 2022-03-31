age = int(input())
washer_price = float(input())
toy_price = int(input())
toys = 0
money = 0
money1 = 0
for i in range (1, age + 1):
    if i % 2 == 0:
        money1 += 10
        money += money1
        money -= 1
    else:
        toys += 1

toy_total = toys * toy_price
total_money = toy_total + money
diff = abs(total_money - washer_price)
if total_money >= washer_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
