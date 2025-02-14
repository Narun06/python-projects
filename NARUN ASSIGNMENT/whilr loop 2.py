number = int(input("Enter a number to find its factorial: "))
factorial = 1
count = 1

while count <= number:
    factorial *= count
    count += 1

print(f"The factorial of {number} is: {factorial}")
