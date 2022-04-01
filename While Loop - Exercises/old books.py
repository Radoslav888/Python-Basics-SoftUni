book = str(input())
count = -1
while True:
    current_book = str(input())
    count += 1
    if current_book == book:
        print(f"You checked {count} books and found it.")
        break
    elif current_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {count} books.")
        break