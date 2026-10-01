# Student Name: Miguel Garcia
# Course Number: CMP 131
# Week Number: 6
# Lab Number: 1
# Assignment Title: Mobile Phone Service Bill
# Date: 10/01/2026

print("----------------------------------------")
print("       MOBILE PHONE SERVICE BILL")
print("----------------------------------------")

print("Package A")
print("  Monthly Charge: $39.99")
print("  Included Minutes: 450")
print("  Additional Minutes: $0.45 per minute")
print()

print("Package B")
print("  Monthly Charge: $59.99")
print("  Included Minutes: 900")
print("  Additional Minutes: $0.40 per minute")
print()

print("Package C")
print("  Monthly Charge: $69.99")
print("  Included Minutes: Unlimited")
print("  Additional Minutes: No additional charge")
print()

package = input("Enter your package (A, B, or C): ").upper()
minutes =int(input("Enter the amount of minutes used: "))

if package in( "A" , "B" , "C" ): 
    print("Valid package")
else: 
    print("Invalid package")