# Sum of digits of the given numbers.
def sum_of_digits(number):
    number_str = str(number)
    total = 0
    for digit in number_str:
        total += int(digit)
    return total


number = int(input('Enter the number:'))
sum_of_digits = sum_of_digits(number)
print(f"Sum of digits of the given numbers is:{sum_of_digits}")

