import numpy as np
import pandas as pd
ps1=pd.Series(range(5),index=['a','b','c','d','e'])
print(ps1['a':'c'])
print(ps1.loc['a':'c'])

array=np.arange(0,12).reshape(3,4)
df=pd.DataFrame(array,index=['a','b','c'],columns=['A','B','C','D'])
print(df.loc['b':,'A':'C'])
df=pd.DataFrame(df)
#loc无末尾减行，iloc有
np.random.randn(5,4)