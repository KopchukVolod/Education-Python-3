bills = [115, 120, 42]

def total_bill(func, bills):
    new_bills = []
    for i in range(len(bills)):
        total = func(bills[i])
        new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")
    return new_bills

def add_tax(total):
     tax = total * 0.06
     new_total = total + tax
     return new_total

def add_tip(total):
    tip = total * 0.2
    new_total = total + tip
    return new_total
 
bills_w_tax = total_bill(add_tax, bills)
print(bills_w_tax)

bills_w_tip = total_bill(add_tip, bills)
print(bills_w_tip)
