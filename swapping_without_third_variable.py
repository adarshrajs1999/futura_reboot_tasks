# Program to swap two numbers without using the third variable.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print(f"Numbers before swapping:num1={num1},num2={num2}")

num1,num2=num2,num1

print(f"After swapping:num1={num1},num2={num2}")
