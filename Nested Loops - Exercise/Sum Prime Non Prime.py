command = input()
non_prime = 0
prime = 0
while command != 'stop':
    command = int(command)
    if command < 0:
        print("Number is negative.")
    else:
        number_is_prime = True

        for i in range(2, command):
           if command % i == 0:
              number_is_prime = False
              break
        if number_is_prime:
           prime += command
        else:
            non_prime += command
    command = input()

print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")