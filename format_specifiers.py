price1 = 3.14354
price2 = -488.58
price3 = 12.23

#Default printing
print ( "Default-------------------------------------------")
print ( f"price1 is {price1}")
print ( f"price2 is {price2}")
print ( f"price3 is {price3}")

#Left padding
print ( "Left Padding--------------------------------------------")
print ( f"price1 is {price1:10}")
print ( f"price2 is {price2:10}")
print ( f"price3 is {price3:10}")

#Write padding
print ( "Write Padding--------------------------------------------")
print ( f"price1 is {price1:<10}")
print ( f"price2 is {price2:<10}")
print ( f"price3 is {price3:<10}")

#Number of decimal places
print ( "Number of decimal Places--------------------------------------------")
print ( f"price1 is {price1:.2f}")
print ( f"price2 is {price2:.2f}")
print ( f"price3 is {price3:.2f}")

#Both padding & decimal places
print ( "Pading & decimal Places--------------------------------------------")
print ( f"price1 is {price1:10.2f}")
print ( f"price2 is {price2:10.2f}")
print ( f"price3 is {price3:10.2f}")

