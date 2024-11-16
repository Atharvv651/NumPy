import numpy as np

data_types = [('name', 'S15'), ('class', int), ('height', float)]

array = [
    ('Jake', 5, 100.2),
    ('Paul', 6, 120.5),
    ('Mia', 4, 95.3),
    ('Lily', 7, 105.8),
    ('Evan', 5, 98.7)
]

array = np.array(array, dtype=data_types)

print("Original Array: \n")
print(array)

print("Sorted According To Height (Ascending): \n")
print(np.sort(array, order='height'))

print("Sorted According To Height (Descending): \n")
print(np.flip(np.sort(array, order='height')))
