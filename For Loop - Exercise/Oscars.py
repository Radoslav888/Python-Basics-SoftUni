actor = str(input())
points = float(input())
jury = int(input())

for i in range(jury):
    name = input()
    points_jury = float(input())
    final_points = len(name) * points_jury / 2
    points += final_points
    if points >= 1250.5:
        break

diff = 1250.5 - points
if points > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {actor} you need {diff:.1f} more!")