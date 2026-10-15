#AUTOMATED SHIPPING FEE CALCULATOR
print("SHIPPING FEE CALCULATOR \n")

is_vip = input("Are you having A VIP membership (Yes or No): ").upper().strip()

if is_vip == "YES":
    print("Shipping Cost is Free.")
elif is_vip == "NO":
    print("Package Weight to Cost Section\n")
    
    weight = float(input("Enter Weight of Package (kg): "))

    if weight <= 2:
        print("Price is $5.00 for your package.\n")
    elif 2 < weight <= 10:
        print("Price is $12.00 for your package.\n")
    elif 10 < weight <= 50:
        print("Price is $25.00 for your package.\n")
    else:
        print("Package Is OVERWIEGHT...!!!\n")
        print("Reduce It Or Cannot Be Shipped.\n")

else:
    print("Please Provide A 'YES' or 'NO' Response...")

