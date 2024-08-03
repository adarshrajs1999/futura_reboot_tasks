# Checking wheather a given number is prime or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(1))