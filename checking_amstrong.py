# Checking whether a given number is amstrong.
def is_armstrong(number):
    number_str = str(number)
    power = len(number_str)
    power_sum = sum([(int(i)) ** power for i in number_str])
    return power_sum == number


print(is_armstrong(153))
print(is_armstrong(234))