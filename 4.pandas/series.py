import numpy as np
import pandas as pd
a=[1,2,3]
myvar=pd.Series(a)
print(myvar)#加了一列行的索引值标签
a2=np.array([1,2,3,4])
myvar2=pd.Series(a2,index=['a','b','c','d'])
print(myvar2)