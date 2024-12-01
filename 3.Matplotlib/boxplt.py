import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_csv('BMI_boxplot.csv')
data.boxplot(column='BMI',by='region')
regions=['1','2','3','4','5','6','7','8','9']
plt.xticks(range(1,10), regions)
plt.show()


