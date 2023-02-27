weight = 4.8
#Ground shipping
if weight <= 2:
  Ground_shipping_weight = weight * 1.50 + 20
elif (weight > 2) and (weight <= 6):
   Ground_shipping_weight = weight * 3 + 20
elif (weight > 6) and (weight <= 10):
  Ground_shipping_weight = weight * 4 + 20
else:
  Ground_shipping_weight = weight * 4.75 + 20
print("Ground_shipping_weight $", Ground_shipping_weight)

#Premnium shipping
Premnium_shipping = 125
print("Premnium_shipping $", Premnium_shipping)

#Dron shipping 
if weight <= 2:
  Dron_shipping = weight * 4.50 
elif (weight > 2) and (weight <= 6):
   Dron_shipping = weight * 9 
elif (weight > 6) and (weight <= 10):
  Dron_shipping = weight * 12 
else:
  Dron_shipping = weight * 14.25
print("Dron_shipping $", Dron_shipping)



