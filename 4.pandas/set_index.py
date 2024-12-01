import pandas as pd
import numpy as np

colnames=['Name','Time','Course']
df=pd.DataFrame([['Jay',10,'python'],['Raj',12,'C++'],['Jack',11,'perl']],columns=colnames)
print(df)
print(df.set_index('Name'))#改变索引值，直接去掉原来的列数字索引，用Name列做索引
print(df)
df.set_index('Name',inplace=True)
print(df)