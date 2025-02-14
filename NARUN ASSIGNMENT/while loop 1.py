n = int(input("Enter how many numbers you want to sum: "))
total_sum = 0
count = 0

while count < n:
    number = float(input(f"Enter number {count + 1}: "))
    total_sum += number
    count += 1

print("The sum of the numbers is:", total_sum)
