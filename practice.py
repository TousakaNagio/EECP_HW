import matplotlib.pyplot as plt
x = list(range(1,6))
y1 = [x**-1 for i in x]
plt.plot(x,y1)

plt.show()