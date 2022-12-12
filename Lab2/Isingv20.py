#Adam Ignaciuk Python w zastosowaniach naukowych laboratorium drugie

#Ising model in 2D with Monte Carlo algorithm

import numpy as np
import random as random
import tqdm
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw
from matplotlib.animation import FuncAnimation

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

    def randomspins(self):
        np.zeros((self.M, self.N))
        spins = np.random.randint(0, 2, (self.M, self.N))
        for i in range(M):
            for j in range(N):
                if spins[i,j] == 0:
                    spins[i , j] = -1
        return spins
    def sumstate(self, spins,i,j):
        #height, width = spins.shape
        #sum_of_states = -spins[i, j]
        for dw in range(-1, 2):
            for dh in range(-1, 2):
                sumprevious = spins[i+dw,j]+spins[i-dw,j]+spins[i,j+dh]+spins[i,j-dh]+spins[i,j]
                sumnow = spins[i+dw,j]+spins[i-dw,j]+spins[i,j+dh]+spins[i,j-dh]-spins[i,j]
        deltaE = (sumnow - sumprevious)
        if deltaE < 0:
            spins[i, j] = -1 * spins[i, j]
        xd = spins
        return xd


J = 1
M = 10
N = 10
B = 1
Beta = 1
img = Image.new('RGB',(M,N), (255,255,255))
draw = ImageDraw.Draw(img)
a = IsingModel(J=J,M=M, N=N, B=B, Beta=Beta)
spins = a.randomspins()
print(spins)
xd = []
for i in range(M-2):
    for j in range(N-2):
        b = a.sumstate(spins,i,j)
        xd.append(b)
print(spins)
rectangle = []

for i in range(M):
    for j in range(N):
        shape = [(i, j), (i, j)]
        if spins[i,j] == 1:
            r = draw.rectangle(shape, (255, 255, 255), width=1)
        else:
            r = draw.rectangle(shape, (0, 0, 0), width = 1)

fig, ax = plt.subplots()
def update(i):
    axis = xd[i]
    ax.imshow(axis, cmap='gray')
    ax.set_axis_off()

anim = FuncAnimation(fig, update, frames=20, interval=500)
plt.show()



