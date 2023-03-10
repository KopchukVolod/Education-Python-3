# You manage the largest shipping company in the region of three districts, SAL's Shippers. You want to make sure that each client has the best and most accessible experience of delivery of their parcels. This project requires a program to calculate the package weight and determine the most cost-effective way to send this package using SAL's Shippers.
SAL's Shippers offers several different options for sending a parcel to a client:
Ground delivery, which is a small fixed fee plus a tariff based on the weight of your package. Ground delivery Premium, which is much higher fixed price, but you are not charged for weight. Unmanned delivery (new), which does not provide a fixed fee, but the weight-based tariff is three times higher than the ground delivery rate.

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
