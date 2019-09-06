import time
import matplotlib.pyplot as plt
import math

plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()
i = 0
x, y = [], []

while True:

    a = 5 * math.sin(2 * (math.pi) * i)
    func = 3 * (math.pi) * (math.exp(-a))
    print(i, func) #i, func
    x.append(i)
    y.append(func)
    i += 1

    ax.plot(x, y, color='b')

    fig.canvas.draw()

    ax.set_xlim(left=max(0, i-50), right=i+50)
    time.sleep(0.1)
    #plt.close()
