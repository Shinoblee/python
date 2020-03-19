import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)
# print(array.shape)

array = np.zeros((3, 4), dtype=int)
array = np.ones((3, 4), dtype=int)
array = np.full((3, 4), 5, dtype=int)
array = np.random.random((3, 4))
# print(array)
# print(array[0, 0])
# print(array > 0.2)

# print(array[array > 0.2])
dimension_inch = np.array([1, 2, 3])
dimension_cm = dimension_inch * 2.54
print(dimension_cm)
