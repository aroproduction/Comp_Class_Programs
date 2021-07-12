# Python program to convert decimal into other number systems

dec = int(input("Enter a Decimal Integer: "))

print("\n"+"The decimal value of", dec, "is:")
print(bin(dec)[2:], "in binary.")
print(oct(dec)[2:], "in octal.")
print(hex(dec)[2:], "in hexadecimal."+"\n")
