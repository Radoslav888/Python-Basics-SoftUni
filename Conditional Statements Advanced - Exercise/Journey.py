budget = float(input())
season = str(input())

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_to_sleep = "Camp"
        price = 0.3 * budget
    if season == "winter":
        place_to_sleep = "Hotel"
        price = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = 0.4 * budget
        place_to_sleep = "Camp"
    if season == "winter":
        place_to_sleep = "Hotel"
        price = budget * 0.8

elif budget > 1000:
    destination = "Europe"
    place_to_sleep = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place_to_sleep} - {price:.2f}")
