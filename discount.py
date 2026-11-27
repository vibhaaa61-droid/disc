amount = float(input("Enter purchase amount: "))

if amount < 2000:
    discount = amount * 0.05
elif amount <= 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.15
discounted_amount = amount - discount
gst = discounted_amount * 0.05    

final_amount = discounted_amount + gst

print("Discount:", discount)
print("Amount after discount:", discounted_amount)
print("GST:", gst)

print("Final Amount:", final_amount)
