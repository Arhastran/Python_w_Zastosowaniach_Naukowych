import numpy as np
from numpy import random as random
import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors as c
import tqdm


class IsingModel:
    def __init__(self , spins =[],  M = 1, N=1 , B = 1, Beta= 1, J = 1, T = 10, ran=10, steps = 10,density =0.5):
        self.spins = spins
        self.M = M
        self.N = N
        self.B = B
        self.Beta = Beta
        self.J = J
        self.T = T
        self.steps = steps
        self.datay = []
        self.ran = ran
        self.T = T
        self.fig, self.ax = plt.subplots()
        self.cMap = c.ListedColormap(['black', 'white'])
        self.density = density

    def randomspins(self):
        np.zeros((self.M, self.N))
        spins = np.random.randint(0, 2, (self.M, self.N))
        for i in range(self.M):
            for j in range(self.N):
                if spins[i, j] == 0:
                    spins[i, j] = -1
        return spins
    def randombetter(self):
        spins = np.random.choice([1, -1], size=(self.M, self.N), p=[self.density, 1 - self.density])
        return spins

    def testrandomspins(self):
        spins = np.ones((self.M, self.N))
        return spins

    def hamiltonian(self, spins1, spins2):
        return (-self.J * (spins1 + spins2) - self.B * (spins2))

    def sumstate(self, spins):
        new_spins=copy.deepcopy(spins)
        for n in range(self.ran):
            i = np.random.randint(self.M - 1)
            j = np.random.randint(self.N - 1)
            field = new_spins[i+1,j]+new_spins[i-1,j]+new_spins[i,j+1]+new_spins[i,j-1]
            previous = field + new_spins[i,j]
            current = field - new_spins[i,j]
            energyBefore = self.hamiltonian(field,previous)
            energyAfter= self.hamiltonian(field,current)
            deltaE = (energyAfter - energyBefore)
            if deltaE < 0:
                new_spins[i, j] = -1 * new_spins[i, j]
            elif np.random.uniform(0, 1) < np.exp(-1 / self.T * deltaE):
                new_spins[i, j] = -1 * new_spins[i, j]
        return new_spins

    def simulate(self, spins):
        for i in tqdm.tqdm(range(self.steps)):
            if  i == 0:
                self.datay.append(spins)
            self.datay.append(self.sumstate(self.datay[i]))
        return self.datay

    def update(self, i):
        #self.ax.imshow(self.datay[i])
        #self.ax.set_axis_off()
        plt.pcolormesh(self.datay[i], cmap=self.cMap)

    def animate(self):
        frames = self.steps
        self.anim = FuncAnimation(self.fig, self.update, frames=frames, interval=1000/frames)
        self.fig.set_size_inches(10, 7.5)
        plt.title("Ising model simulation")
        #self.anim.save(f'{"Ising simulation"}.gif', writer='pillow')
        plt.show()


J = 1
M = 200
N = 200
B = 1/2
Beta = 1
ran = 200
steps = 200
density = 0.1

a = IsingModel(J=J,M=M, N=N, B=B, Beta=Beta,ran=ran,steps=steps,density=density)
HAHA = a.randombetter()
dzialajpls = a.simulate(HAHA)
a.animate()

#arr = a.simulate(random)


