# 1.Check whether the given number is even or add.
def check_even(num):
    if num%2 ==0:
        return 'even'
    else:
        return 'odd'

print(check_even(25))
print(check_even(24))