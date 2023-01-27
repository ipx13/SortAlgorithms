def sort(set_data):
    for x in range(set_size):
        for y in range(0, (set_size - x) - 1):
            if set_data[y] > set_data[y + 1]:
                set_data[y], set_data[y + 1] = set_data[y + 1], set_data[y]

set_data = [100, 49, 55, 90, 47, 29, 97, 39, 42, 44]
set_size = len(set_data)

print('\n----- Bubble Sort Demonstration -----\n')
print('Before applying bubble sort:')
print(set_data)

sort(set_data)
print('\nAfter applying bubble sort:')
print(set_data)