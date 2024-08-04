# Check whether given number is palindrome

def check_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter the number to check:"))
if check_palindrome(num):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome.")
print(num)

