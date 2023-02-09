#Adam Ignaciuk Python w zastosowaniach naukowych laboratorium drugie

#Ising model in 2D with Monte Carlo algorithm

import numpy as np
import random as random
import tqdm
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
import matplotlib.animation
from matplotlib.animation import FuncAnimation, writers
from IPython import display
from matplotlib import colors as c
import matplotlib.animation as animation


class IsingModel:
    def __init__(self , spin = 0, spins =[],  M = 1, N=1 , B = 1, Beta= 1, J = 1, file = ''):
        self.spins = spins
        self.spin = spin
        self.file = file
        self.M = M
        self.N = N
        self.B = B
        self.Beta = Beta
        self.J = J
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.line, = self.ax.plot([], [], lw=2)

    def randomspins(self):
        np.zeros((self.M, self.N))
        spins = np.random.randint(0, 2, (self.M, self.N))
        for i in range(self.M):
            for j in range(self.N):
                if spins[i,j] == 0:
                    spins[i , j] = -1
        return spins
    def testrandomspins(self):
        spins = np.ones((self.M, self.N))
        return spins

    def hamiltonian(self, spins1, spins2):
        return (-self.J*(spins1+spins2)-self.B*(spins2))

    def sumstate(self, spins,i,j):
       # for dw in range(-1, 2):
       # for dh in range(-1, 2):
        field = spins[i+1,j]+spins[i-1,j]+spins[i,j+1]+spins[i,j-1]
        previous = field + spins[i,j]
        current = field - spins[i,j]
        energyBefore = self.hamiltonian(field,previous)
        energyAfter= self.hamiltonian(field,current)
        deltaE = (energyAfter - energyBefore)
        print(energyBefore)
        print(energyAfter)
        print(deltaE)
        if deltaE > 0:
            spins[i, j] = -1 * spins[i, j]
        return spins

    def changing(self,spins, ran):
        xd = spins
        for n in range(ran):
            i = np.random.randint(self.M-1)
            j = np.random.randint(self.N-1)
            xd = self.sumstate(xd,i,j)
        return xd

    def set_data(self, datay):
        self.datay = datay

    def ani_update(self, i):
        y = self.datay[i]
        cMap = c.ListedColormap(['black', 'white'])
        plt.pcolormesh(y, cmap=cMap)


    def animate(self):
        self.anim = animation.FuncAnimation(self.fig, self.ani_update, frames=self.M, interval=20, blit=False)
        plt.show()
        self.anim.save(f'{"Title"}.gif', writer='pillow')

J = 1
M = 30
N = 30
B = 1/2
Beta = 1

a = IsingModel(J=J,M=M, N=N, B=B, Beta=Beta)
spins = a.testrandomspins()
xd = []
xd.append(spins)
for i in range(10):
    xd.append(a.changing(xd[i],30))
#print(spins)
#print(xd)

img = Image.new('RGB',(M,N), (255,255,255))
draw = ImageDraw.Draw(img)

a.set_data(xd)
a.animate()
#for element in range(number+1):
#    aha = xd[element]
#    for i in range(M):
#        for j in range(N):
#            shape = [(i, j), (i, j)]
#            if aha[i, j] == 1:
#                r = draw.rectangle(shape, (255, 255, 255), width=1)
#            else:
#                r = draw.rectangle(shape, (0, 0, 0), width=1)
#    img.save('/Users/adamignaciuk/PycharmProjects/PythonwZastosowaniachNaukowych/Lab2/img'+str(element)+'.png')

