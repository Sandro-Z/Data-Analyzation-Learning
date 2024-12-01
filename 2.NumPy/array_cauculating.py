import numpy as np

arr1=np.arange(0,1,0.01)
print(arr1)
arr2=np.random.randn(100)
print(arr2)

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

print(np.sum(arr2))
print(np.mean(arr2))
print(np.std(arr2))
print(np.var(arr2))
print(np.argmin(arr2))