# Student Name: Miguel Garcia
# Course Number: CMP 131
# Week Number: 6
# Lab Number: 1
# Assignment Title: Software Quantity Discount
# Date: 10/01/2026


print("----------------------------------------")
print("       SOFTWARE QUANTITY DISCOUNT")
print("----------------------------------------")


price_per_unit = 99.00


units_purchased = int(input("Enter the number of units purchased: "))


if units_purchased <= 0:
    print("Error: The number of units must be greater than 0.")

else:
   
    original_cost = units_purchased * price_per_unit

    if units_purchased < 10:
        discount_rate = 0.00
    elif units_purchased <= 19:
        discount_rate = 0.20
    elif units_purchased <= 49:
        discount_rate = 0.30
    elif units_purchased <= 99:
        discount_rate = 0.40
    else:
        discount_rate = 0.50

    
    discount_amount = original_cost * discount_rate
    final_cost = original_cost - discount_amount

    
    print()
    print("----------------------------------------")
    print("            PURCHASE REPORT")
    print("----------------------------------------")
    print(f"Units Purchased:       {units_purchased}")
    print(f"Price Per Unit:        ${price_per_unit:.2f}")
    print(f"Original Cost:         ${original_cost:,.2f}")
    print(f"Discount Percentage:   {discount_rate * 100:.0f}%")
    print(f"Discount Amount:       ${discount_amount:,.2f}")
    print(f"Final Cost:            ${final_cost:,.2f}")
    print("----------------------------------------")