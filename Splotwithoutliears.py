import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(50)
y=-x + np.random.normal(0, 0.1, 50)
x=np.append(x,0.2)
y=np.append(y,0.2)
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('negative correlation with outliers')
plt.show()