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
        self.images = []

    def randomspins(self):
        np.zeros((self.M, self.N))
        spins = np.random.randint(0, 2, (self.M, self.N))
        for i in range(self.M):
            for j in range(self.N):
                if spins[i,j] == 0:
                    spins[i , j] = -1
        return spins

    def sumstate(self, spins,i,j):
       # for dw in range(-1, 2):
        #    for dh in range(-1, 2):
        sumprevious = spins[i+1,j]+spins[i-1,j]+spins[i,j+1]+spins[i,j-1]+spins[i,j]
        sumnow = spins[i+1,j]+spins[i-1,j]+spins[i,j+1]+spins[i,j-1]-spins[i,j]
        deltaE = (sumnow - sumprevious)
        if deltaE < 0:
            spins[i, j] = -1 * spins[i, j]
        return spins

    def changing(self,spins, ran):
        xd = []
        xd.append(spins)
        for n in range(ran):
            i = np.random.randint(self.M-1)
            j = np.random.randint(self.N-1)
            print(i,j)
            xd.append(self.sumstate(xd[n],i,j))
            print(xd[n])
        return xd, n

J = 1
M = 10
N = 10
B = 1
Beta = 1

a = IsingModel(J=J,M=M, N=N, B=B, Beta=Beta)
spins = a.randomspins()
xd, number = a.changing(spins,5)
#print(spins)
#print(xd)

img = Image.new('RGB',(M,N), (255,255,255))
draw = ImageDraw.Draw(img)

for element in range(number):
    aha = xd[element]
    for i in range(M):
        for j in range(N):
            shape = [(i, j), (i, j)]
            if aha[i, j] == 1:
                r = draw.rectangle(shape, (255, 255, 255), width=1)
            else:
                r = draw.rectangle(shape, (0, 0, 0), width=1)
    img.save('/Users/adamignaciuk/PycharmProjects/PythonwZastosowaniachNaukowych/Lab2/img'+str(element)+'.png')





