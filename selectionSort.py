def sort(set, set_size):
    for x in range(set_size):
        min = x
        for y in range(x + 1, set_size):
            if set[y] < set[min]:
                min = y

        (set[x], set[min]) = (set[min], set[x])

set_data = [100, 49, 55, 90, 47, 29, 97, 39, 42, 44]
set_size = len(set_data)

print('\n----- Selection Sort Demonstration -----\n')
print('Before applying selection sort:')
print(set_data)

sort(set_data, set_size)
print('\nAfter applying selection sort:')
print(set_data)