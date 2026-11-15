import numpy as np

l1 = [1, 2, 3, 4, 5]
print(type(l1))
print(l1)

#Creating an Array
# 1. Using the list to create an array
sampleArray = np.array(l1)
print(type(sampleArray))
print(sampleArray)

#2D Array
allZeroArray = np.zeros((3, 2))
allOneArray = np.ones((5, 4))
a1 = np.arange(20)

arrays = [allZeroArray, allOneArray, a1]

for i in arrays:
    print('Array: \n', i)
    print('Dimensions: ', i.ndim)
    print('Shape: ', i.shape)
    print('Size: ', i.size)
    print('Memory Bytes: ', i.nbytes)
    print('-' * 100)

#Converting 1D to 2D Array
a2 = np.arange(14, 26)
print(a2)

a3 = np.arange(14, 26).reshape(2, 6)