def slice_less(my_list, lesser):
    new_list = []
    for elem in my_list:
        if elem > lesser:
            new_list.append(elem)
    return  sorted(new_list)[::-1]

print(slice_less([2,2,8,4,3,56,0,-34,9], 5))