number = int(input("Enter a number: "))
sum_of_factors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_factors += i

if sum_of_factors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
