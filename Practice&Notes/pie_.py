import numpy as np
import matplotlib.pyplot as plt
labels=['A','B','C','D']
size=[50,30,15,5]
plt.pie(size,labels=labels,autopct='%1.1f%%',startangle=140)
plt.show()