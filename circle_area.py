# Calculating circle area:

import math

def calculate_circle_area(r):
    return math.pi*(r**2)

r = float(input("Enter the radius of the circle:"))
print(f"r = {r}\nArea = {calculate_circle_area(r)}")
