import sys
digit_string = sys.argv[1]

sum_numbers = []
for number in digit_string:
    sum_numbers.append(int(number))

print(sum(sum_numbers))
