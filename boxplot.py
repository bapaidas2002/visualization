import matplotlib.pyplot as plt

weights = [30,20,10,15,5,10,25,35]

plt.boxplot(weights)

plt.xlabel('Weights')
plt.title('Box plot of box weights')

plt.show()