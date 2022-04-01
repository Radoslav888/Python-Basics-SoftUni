width = int(input())
lenght = int(input())
height = int(input())
volume = width * lenght * height
is_there_more_free_space = True
command = input()
while command != "Done":
    number_of_boxes = int(command)
    volume -= number_of_boxes
    if volume < 0:
        is_there_more_free_space = False
        break
    command = input()

if is_there_more_free_space:
    print(f"{volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")