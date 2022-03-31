length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = (length * width * height) / 1000
ocupied_volume = percent / 100
needed_litres = aquarium_volume * (1 - ocupied_volume)

print(needed_litres)

