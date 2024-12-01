import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.5)
y=np.sin(x)
plt.figure()
plt.bar(x,y,width=0.5,color='cyan',edgecolor='k')

plt.show()
plt.hist(y,10)
plt.show()