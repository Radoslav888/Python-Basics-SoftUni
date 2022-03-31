type = str(input())
rows = int(input())
columbs = int(input())
price = 0
if type == "Premiere":
    price = 12
    total_sits = rows * columbs
    total_price = total_sits * price
elif type == "Normal":
    price = 7.5
    total_sits = rows * columbs
    total_price = total_sits * price
if type == "Discount":
    price = 5
    total_sits = rows * columbs
    total_price = total_sits * price
print(f'{total_price:.2f} leva')