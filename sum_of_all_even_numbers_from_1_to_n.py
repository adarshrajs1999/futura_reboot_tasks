# sum of all even numbers from 1 to n

def sum_of_evens(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total


print(sum_of_evens(5))


