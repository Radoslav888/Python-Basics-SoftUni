from math import pi

figure_type = str(input())

if figure_type == "square":
    side = float(input())
    area = side * side
    print(f'{area:.3f}')

elif figure_type == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area_r = side1 * side2
    print(f'{area_r:.3f}')

elif figure_type == "circle":
    radius = float(input())
    area_c = (radius ** 2) * pi
    print(f'{area_c:.3f}')

elif figure_type == "triangle":
    side_t = float(input())
    height = float(input())
    area_t = (side_t * height) / 2
    print(f'{area_t:.3f}')