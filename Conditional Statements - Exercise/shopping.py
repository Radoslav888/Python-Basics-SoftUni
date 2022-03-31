budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

gpu_price = gpu * 250
cpu_price = (0.35 * gpu_price) * cpu
ram_price = (0.1 * gpu_price) * ram

final_sum = gpu_price + cpu_price + ram_price

if gpu > cpu:
    final_sum *= 0.85

money_left = abs(budget - final_sum)

if final_sum <= budget:
    print(f"You have {money_left:.2f} leva left!")

else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")