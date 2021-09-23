str_1 = input("Enter elements of a list separated by space: ")
str_2 = input("Enter elements of a list separated by space: ")

list_of_str_1 = str_1.split(' ')
list_of_str_2 = str_2.split(' ')

list_of_int_1 = []
list_of_int_2 = []

for char_inn in list_of_str_1:
    int_inn = int(char_inn)
    if (int_inn in list_of_int_1) != True:
        list_of_int_1.append(int_inn)
        
for char_inn in list_of_str_2:
    int_inn = int(char_inn)
    if (int_inn in list_of_int_2) != True:
        list_of_int_2.append(int_inn)
        
list_of_int_1 = sorted(list_of_int_1)
list_of_int_2 = sorted(list_of_int_2)

print("set 1: {}".format(list_of_int_1))
print("set 2: {}".format(list_of_int_2))


Intersection_list = []

for number in list_of_int_1:
    if number in list_of_int_2:
        Intersection_list.append(number)
        
for number in list_of_int_2:
    if number in list_of_int_1 and (number in Intersection_list) != True:
        Intersection_list.append(number)

print("Intersection: {}".format(Intersection_list))


union_list_dummy = list_of_int_1 +list_of_int_2
union_list = []
for char_inn in union_list_dummy:
    int_inn = int(char_inn)
    if (int_inn in union_list) != True:
        union_list.append(int_inn)
union_list = sorted(union_list)
        
print("Union: {}".format(union_list))


