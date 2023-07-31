# Numpy - Numerical Python

import numpy as np

                                                # Python List vs Numpy array on basis of time of execution

# from time import process_time

'''python_list = [i for i in range(10000)]
start_time = process_time()
python_list = [i+5 for i in python_list]
end_time = process_time()
print(f"Time taken by list: {end_time-start_time}")  # output 0.001772

np_array = np.array([i for i in range(10000)])
start_time = process_time()
np_array += 5 
end_time = process_time()
print(f"Time taken by numpy array: {end_time-start_time}") # output 0.000646'''

                                                # Numpy Array

'''np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
print(type(np_array))
print(np_array.shape)'''

                                                # Numpy Matrix

'''np_matrix = np.array([[1,2,3],[4,5,6]])
print(np_matrix)
print(np_matrix.shape)'''

                                                # Numpy Float Array

'''np_float_array = np.array([[1,2,3],[4,5,6]], dtype = float)  # dtype = data type
print(np_float_array)'''

                                                # Initialising numpy array with 0's and 1's and particular value

'''ones_array = np.ones((3,4))
zeros_array = np.zeros((3,4))
any_number_array = np.full((3,4), 10)  # full(shape, specific_number)
print(ones_array)
print(zeros_array)
print(any_number_array)'''

                                                # Creating Identity matrix 

'''identity_matrix = np.eye(5)
print(identity_matrix)'''

                                                # Creating Numpy array of random values

'''random_value_matrix = np.random.random((3,4))
print(random_value_matrix)'''

                                                # Creating Random integer value array

'''random_int_value_matrix = np.random.randint(1,100,(3,4))   # randint(range from, range to, shape)
print(random_int_value_matrix)'''

                                                # Array of evenly spaced value

'''evenly_spaced_array = np.linspace(10, 30, 6)   # linspace(range start, range to, number of values required)
print(evenly_spaced_array)

evenly_spaced_array_step = np.arange(10,30,5)  # arange(range start, range to, step between next value)
print(evenly_spaced_array_step)'''

                                                # Convert a list to array

'''list1 = [1,2,3,4,5]
print(list1)
np_array = np.asarray(list1)
print(np_array)'''

                                                # Analysing Numpy Array

'''matrix = np.random.randint(1, 100, (5,5))

print(matrix.shape)   # Shows the order of array
print(matrix.ndim)    # Shows the dimension of array
print(matrix.size)    # Shows the no. of element present in array or matrix
print(matrix.dtype)   # Shows the data type of element present in numpy array'''

                                                # Mathematical operations on numpy array

'''array1 = np.random.randint(1,10, (3,3))
array2 = np.random.randint(1,10, (3,3))
print(array1)
print(array2)
print(array1 + array2)   # alternative np.add(array1, array2)
print(array1 - array2)   # alternative np.subtract(array1, array2)
print(array1 * array2)   # alternative np.mutliply(array1, array2)
print(array1 / array2)   # alternative np.divide(array1, array2)'''

                                                # Array Manipulation

array = np.random.randint(0,10, (2,3))
print(array)
trans = np.transpose(array)   # Converts the array to transpose of array
trans1 = array.T              # alternative - Converts the array to transpose
print(trans1)
print(trans.shape)

array1 = array.reshape(3,2)   # Reshapes the array
print(array1)