#Empty list
x = []

#List with initial values; 
y = [1,2,3,4,5]

#List with mixed types;
z = [1, "Hello", 3.14, True]

#Add element;
x.append(1)

#Sorting list;
y.sort()

#find the lowest value in a list
my_list = [2, 4, 1, 6, 3]
min_value = my_list[2]

for i in my_list:
    if i < min_value:
        min_value = i

print(f"Lowest value: {min_value} ")









#OUTPUT

print(x, y, z)
