# import numpy as np
# print("1D array")
# a=np.array([1,2,3,4])
# print(a)

# print("2d array")
# a2=np.array([[1,4,5],[3,4,5]])
# print(a2)

# b=np.array([[1,2,3],[6,6,8]])
# print(b.shape)

# print(b.ndim)

# print(b.size)
# print(b.dtype)
# print(b.itemsize)


# # array creation => (zeros),(ones),linspace,eye,arange

# import numpy as np
# arr = np.zeros((3,3))
# print(arr)

# arr=np.ones((2,4))
# print(arr)

# arr=np.arange(0,10,2)
# print(arr)

# arr=np.linspace(0,10,2)
# print(arr)

# arr=np.eye(3)
# print(arr)


# # Array reshaping and resizing => reshape,ravel,resize

# import  numpy as np
# arr =np.arange(9)
# reshape=arr.reshape(3,3)
# print(reshape)

# print(arr.reshape((3,3)))

# print(arr.ravel())
 
# import numpy as np
# arr=np.array([[1,2,3],[2,4,8]])
# resize=np.resize(arr,(3,3))
# print(resize)

# # Array operations

# import numpy as np
# arr1=np.array([1,2,33])
# arr2=np.array([45,6,8])
# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2) 

# # Universal functions

# print(np.sqrt(arr))
# print(np.exp(arr))

# # board coasting

# import numpy as np
# arr3 = np.array([[4,8,9],[3,4,5]])
# arr4 = np.array([[1,3,4],[3,8,9]])
# result = arr3 + arr4
# print(result)

# # indexing and slicing

# import numpy as np
# ar = np.array([[2,6,8],[2,3,4],[6,8,9]])
# print(ar[2])

# print(ar[[0,2],[1,2]])

# print(ar[1:4])


# Random module => np.random.randint , np.random.rand , np.random.choice

import numpy as np
arr=np.array((2,3))
print(np.random.rand())

arr = np.random.randint([2,1])
print(arr)

arr=np.array([1,2,3,4])
chosn=np.random.choice(arr,3)
print(chosn)


# Mathematical and statistical methods => sum , mean , standard deviation,min,max,argin/argmax

# import numpy as np
# arr1=np.array([1,2,3,4])
# print(np.sum(arr1))
# print(np.mean(arr1))
# print(np.std(arr1))

# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr))
# print(np.argmax(arr))



# Linear Algebra functions
# import numpy as np
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# result = np.dot(a,b)
# print(result)

import numpy as np
a=np.array([[1,2],[3,4]])
det = np.linalg.det(a)
print(det)

inv = np.linalg.inv(a)
print(inv)

