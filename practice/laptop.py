print("==========Welcome to Laptop Bazar==========")
print("1. Dell(Rs:20000) 2. Toshiba(Rs:30000) 3. Mac(Rs:50000)")
product_name=""
dell_price=0
toshiba_price=0
mac_price=0
quantity =0

option = int(input("Enter any option: "))
if option==1:
    quantity = int(input("Enter quantity: "))
    product_name="Dell"
    dell_price=quantity*20000

elif option==2:
    quantity = int(input("Enter quantity: "))
    product_name="Toshiba"
    toshiba_price=quantity*30000

elif option==3:
    quantity = int(input("Enter quantity: "))
    product_name="Mac"
    mac_price=quantity*50000

else:
    print("Invalid option")
    exit()


print("Delivery Option: 1. Home(Rs:1000) 2. Pickup(Rs:0)")
delivery_price=0
delivery_option=int(input("Enter delivery option: "))
if delivery_option==1:
    delivery_price=1000


print("Packing Option 1. Plastic Bag(Rs:1000) 2. Bag(Rs:2000) 3. Gift Box(Rs:5000)")
packing_price=0
packing_option=int(input("Enter packing option: "))
if packing_option==1:
    packing_price=1000
elif packing_option==2:
    packing_price=2000
elif packing_option==3:
    packing_price=5000


total = dell_price + toshiba_price + mac_price 

print("Location .1 KTM(Rs:13%) tax 2. LTP(Free) tax 3. BKT(Free) tax")
tax_amount=0
location_option=int(input("Enter location option: "))
if location_option==1:
    tax_amount=total*0.13


grand_total = total + delivery_price + packing_price + tax_amount
name = input("Enter your name: ")
address = input("Enter your address: ")
phone = input("Enter your phone number: ")
print("==========Invoice==========")
print("Name: ", name)
print("Address: ", address)
print("Phone: ", phone)
print("Product: ", product_name)
print("Quantity: ", quantity)
print("Total: ", total)
print("Delivery Price: ", delivery_price)
print("Packing Price: ", packing_price)
print("Tax Amount: ", tax_amount)
print("Grand Total: ", grand_total)
print("==========Thank you for shopping with us==========")
