import numpy as np
import matplotlib.pyplot as plt
k=20
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])

file= open('xnyn.txt','r')
y=file.readline()
y=y.split(" ")
del y[-1]
y= list(map(float,y))
file.close()








plt.plot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.savefig('../figs/3.3.png')