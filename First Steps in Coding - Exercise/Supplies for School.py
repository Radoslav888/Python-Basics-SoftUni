pencils_package_number = int(input())
markers_package_number = int(input())
litres_cleaning_stuff = int(input())
percent_discount = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
cleaning_stuff = 1.20
needed_sum = pencils_package_number * price_per_pen + \
             markers_package_number * price_per_marker + \
             litres_cleaning_stuff * cleaning_stuff

needed_sum = needed_sum - needed_sum * (percent_discount / 100)
print(needed_sum)