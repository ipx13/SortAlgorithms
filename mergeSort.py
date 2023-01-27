def sort(set_data):
    set_size = len(set_data)
    if set_size > 1:
        left = set_data[:set_size // 2]
        right = set_data[set_size // 2:]

        sort(left)
        sort(right)

        x = 0
        y = 0
        z = 0

        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                set_data[z] = left[x]
                x += 1
            else:
                set_data[z] = right[y]
                y += 1
            z += 1

        while x < len(left):
            set_data[z] = left[x]
            x += 1
            z += 1

        while y < len(right):
            set_data[z] = right[y]
            y += 1
            z += 1

set_data = [100, 49, 55, 90, 47, 29, 97, 39, 42, 44]

print('\n----- Merge Sort Demonstration -----\n')
print('Before applying merge sort:')
print(set_data)

sort(set_data)
print('\nAfter applying merge sort:')
print(set_data)