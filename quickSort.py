def sort(set_data):
    set_size = len(set_data)
    if set_size <= 1:
        return set_data
    else:
        pivot = set_data.pop()

    greater = []
    lower = []

    for x in set_data:
        if x > pivot:
            greater.append(x)

        else:
            lower.append(x)

    return sort(lower) + [pivot] + sort(greater)

set_data = [100, 49, 55, 90, 47, 29, 97, 39, 42, 44]

print('\n----- Quick Sort Demonstration -----\n')
print('Before applying quick sort:')
print(set_data)

print('\nAfter applying quick sort:')
print(sort(set_data))