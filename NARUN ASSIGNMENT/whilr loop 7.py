number = int(input("Enter a number: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    count = 2
    while count <= int(number ** 0.5):
        if number % count == 0:
            is_prime = False
            break
        count += 1

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
