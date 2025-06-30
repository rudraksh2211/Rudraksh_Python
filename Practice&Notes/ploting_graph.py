import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y,label='sin(x)',color='red',linestyle='--')
plt.title('Line Plot of Sin(x)')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
