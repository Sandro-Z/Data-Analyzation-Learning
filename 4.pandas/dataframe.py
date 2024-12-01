import numpy as np
import pandas as pd

array=np.arange(0,12).reshape(3,4)
df=pd.DataFrame(array,index=['a','b','c'],columns=['A','B','C','D'])
print(df)
