list_1 = [0] * 5
list_2 = [0] * 5


def set_list(list):
    for i in range(5):
        list[i] = int(input("Enter a number: "))
    
    return list


def sort_list(lsg):
    lsg.sort()
    print(lsg)


print("Set list 1")
list_1 = set_list(list_1)
print("Set list 2")
list_2 = set_list(list_2)

print("Sort list 1")
sort_list(list_1)
print("Sort list 2")
sort_list(list_2)

list_3 = list_1.__add__(list_2)

print("This is list 3")
print(list_3)
print("This is list 3 after sort")
sort_list(list_3)

