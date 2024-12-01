import pandas as pd
import numpy as np

pd2=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['A', 'B', 'C'])
pd2.loc[4]=[1,1,3]
print(pd2)

pd3=np.arange(12).reshape(3,4)
d1=pd.DataFrame(pd3,index=['a', 'b','c'],columns=['A','B','C','D'])