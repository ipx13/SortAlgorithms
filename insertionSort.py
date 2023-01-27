def sort(set_data):
    for index in range(1, len(set_data)):
        x = set_data[index]
        y = index - 1

        while y >= 0 and x < set_data[y]:
            set_data[y + 1] = set_data[y]
            y -= 1
        set_data[y + 1] = x
    return set_data

set_data = [100, 49, 55, 90, 47, 29, 97, 39, 42, 44]
set_size = len(set_data)

print('\n----- Insertion Sort Demonstration -----\n')
print('Before applying insertion sort:')
print(set_data)

sort(set_data)
print('\nAfter applying insertion sort:')
print(set_data)