import pandas as pd

df=pd.read_csv('csv')
ans=df.loc[1:2,['type','year','price','location']]
ans.to_csv('man!')