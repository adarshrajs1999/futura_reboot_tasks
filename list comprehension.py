# list comprehension of squares all even numbers between 1 and 20.

req_list = [x**2 for x in range(1,21) if x%2 == 0]

print(req_list)