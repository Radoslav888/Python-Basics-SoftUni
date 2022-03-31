pages = int(input())
pages_read_in_1hours = int(input())
days_to_read_the_book = int(input())

hours_to_read_the_whole_book= pages / pages_read_in_1hours
hours_a_day = hours_to_read_the_whole_book / days_to_read_the_book
print(hours_a_day)