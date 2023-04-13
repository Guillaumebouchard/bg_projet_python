my_list = [2, 3, 10, -50, 0, 33, -4, 64, 88, 100, 6, -5, -9, 99]
my_list1 = [2, 3, 10, -50, 0, 33, -4, 64, 88, 100, 6, -5, -9, 99]

def max_list(list):
    maximum = list[0]
    for num in my_list:
        if num > maximum:
            maximum = num
    return maximum

print(max_list(my_list))
print(max(my_list1))

