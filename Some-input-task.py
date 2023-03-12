# Task 1
def total_list(lst):
    suma = 0
    for num in lst:
        suma += num
    return suma

print(total_list([1, 2, 3, 4, 5, 1256, 6, 2, 1, 3, 7, 8, 1256, 1]))

# Task 2
# first possible
num_in_list = [1, 2, 3, 4, 5, 1256, 6, 2, 1, 3, 7, 8, 1256, 1]
x = int(input("Enter the numb :"))
print(num_in_list.count(x)) #enter another num

# second posible
numb_in_list = [1, 2, 3, 4, 5, 1256, 6, 2, 1, 3, 7, 8, 1256, 1]
x = int(input("Enter the numb :"))
count = 0
for i in numb_in_list:
    if i == x:
        count += 1
print("Numb ", x, "in massif", count, "times")

#The third way

x = int(input("Enter the numb :"))
def numb_list(arr):
    count = 0
    for i in arr:
        if i == x:
            count += 1
    return count
print(numb_list([1, 2, 3, 4, 5, 1256, 6, 2, 1, 3, 7, 8, 1256, 1]))




