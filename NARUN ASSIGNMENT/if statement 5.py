salary = float(input("Enter your salary: "))
age = int(input("Enter your age: "))
if salary >= 20000 or age <= 25:
    loan_amount = float(input("Enter required loan amount: "))
    if loan_amount == 50000:
        print("Maximum loan amount is 50000.")
else:
    print("You are not eligible for a loan.")
