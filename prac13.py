qty=float(input("Enter the quantity of item sold:"))
val=float(input("Enter the value of items:"))
discount=int(input("Enter the discount percentage:"))
tax=float(input("Enter the tax amount:"))
amt=qty*val
discount_amt=(amt*discount)/100
sub_total=amt-discount_amt
tax_amt=(sub_total*tax)/100
total_amt=sub_total+tax_amt
print("*********BILL*****************")
print("Quantity sold: \t"+str(qty))
print("Price per item: \t"+str(val))
print("\n \t \t -------------")
print("Amount: \t\t"+str(amt))
print("Discount: \t\t-"+str(discount_amt))
print("    \t \t --------------")
print("Discounted total: \t",sub_total)
print("Tax: \t \t \t +"+str(tax_amt))
print(" \t \t ------------")
print("Total amount to be paid:"+str(total_amt))