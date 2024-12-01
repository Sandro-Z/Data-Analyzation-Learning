import pandas as pd
import numpy as np

pd2=pd.DataFrame(np.arange(9).reshape(3,3),index=['a', 'b','c'],columns=['A', 'B', 'C'])
print(pd2)
pd3=pd2.reindex(['c','b','a','e'])#多加1行，其中元素默认是nan
print(pd3)
print(pd2)#原值不改变，改后输出返回值
pd4=pd2.reindex(columns=['C','B','A'])#索引改变同时改变顺序
print(pd4)
pd5=pd2.reindex(['a','b'])#相当于删行操作
print(pd5)
pd2[4]=9
print(pd2)