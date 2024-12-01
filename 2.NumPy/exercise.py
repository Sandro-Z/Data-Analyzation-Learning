import numpy as np
arr1=np.random.random((3,5))
arr2=np.random.random((3,1))

arr3=arr1**2
print(arr2+arr3)
print(arr2-arr3)
print(arr2*arr3)
print(arr2/arr3)

arr4=arr1[:,1]
arr4[0]=1
print(arr1)#arr1对应位置也变化

arr5=arr1.copy()
arr5[[0,2],[0,4]]=np.NaN
arr5[[0,2],[0,4]]=0
a=arr5.mean(axis=0)
arr5[0,0]=a[0]
arr5[2,4]=a[2]
print(arr5)

print(arr5.mean(axis=1))
print(arr5.max(axis=1))
print(arr5.min(axis=1))