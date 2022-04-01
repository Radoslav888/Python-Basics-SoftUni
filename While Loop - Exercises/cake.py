width = int(input())
lenght = int(input())
pieces = width * lenght
cake_is_over = False
command = input()
while command != 'STOP':
    current_pieces = int(command)
    pieces -= current_pieces
    if pieces < 0:
        cake_is_over = True
        break

    command = input()
if cake_is_over:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{pieces} pieces are left." )