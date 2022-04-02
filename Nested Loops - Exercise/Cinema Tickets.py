students_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
command = input()

while command != "Finish":
    movie_name = command
    free_seats = int(input())
    sold_tickets = 0
    all_seats = free_seats
    while free_seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            students_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        free_seats -= 1
        sold_tickets += 1
        total_tickets += 1

    print(f"{movie_name} - {sold_tickets / all_seats * 100:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{students_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")
