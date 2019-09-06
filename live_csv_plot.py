
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots()

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    t = data['t']
    periodic_func = data['periodic_func']

    plt.cla()
    ax.set_xlim(left=max(0, i-50), right=i+50)
    ax.set_ylim(top=12, bottom=4, auto=True)
    ax.plot(t, periodic_func, label='Live Plotting') #plt

    ax.legend(loc='upper left') #plt
    #ax.tight_layout() #plt


ani = FuncAnimation(fig, animate, interval=1000) #plt.gcf()

#plt.tight_layout()
plt.show()
