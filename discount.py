amount = float(input("Enter purchase amount: "))

if amount < 2000:
    discount = amount * 0.05
elif amount <= 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)