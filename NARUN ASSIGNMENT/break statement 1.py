numbers = [1, 3, 7, 5, 2, 9, 11]
first_even = None

for num in numbers:
    if num % 2 == 0:
        first_even = num
        break

if first_even is not None:
    print("The first even number in the list is:", first_even)
else:
    print("No even numbers found in the list.")
