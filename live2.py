import time
import matplotlib.pyplot as plt
import math
from matplotlib.widgets import Slider, Button, RadioButtons

plt.rcParams['animation.html'] = 'jshtml'
# fig = plt.figure()
# ax = fig.add_subplot(111)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
a0 = 5
f0 = 3
delta_f = 10.0

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()

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
    sfreq = Slider(axfreq, 'Time', 0.1, 30.0, valinit=1, valstep=delta_f)
    samp = Slider(axamp, 'Periodic_func', 0.1, 10.0, valinit=1)

    button.on_clicked(reset)

    ax.plot(x, y, color='b')

    fig.canvas.draw()

    ax.set_xlim(left=max(0, i-50), right=i+50)
    time.sleep(0.1)
    #plt.close()
