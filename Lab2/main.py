#Adam Ignaciuk Python w zastosowaniach naukowych laboratorium drugie

#Ising model in 2D with Monte Carlo algorithm

import numpy as np
import random as random
import tqdm
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageDraw

class IsingModel:
    def __init__(self , spin = 0, spins = [],  M = 1, N=1 , B = 1, Beta= 1, J = 1, file = ''):
        self.spins = spins
        self.spin = spin
        self.file = file
        self.M = M
        self.N = N
        self.B = B
        self.Beta = Beta
        self.J = J

    def randomspins(self, M, N):  # random spins web generator
        spinslist = np.zeros((M,N), dtype = int)
        for i in range(M):
            for j in range(N):
                self.spin = random.randint(0, 1)
                if self.spin == 0:
                    spinslist[i , j] = -1
                else:
                    spinslist[i , j] = 1
        return (spinslist)

    def hamiltonian(self, J,spins):
        sum = np.sum(spins)
        return (-J*sum)

    def possibility(self,beta,energydifference):
        return(np.exp(-beta*energydifference))

    def changestate(self, spin):
        return(spin*-1)
    def magnetisation(self, spins):
        pass
    def imagecreation(self,file):
        img = Image.new('RGB', (1024, 1024), (0, 0, 0))
        return print("Drawed")

    def MonteCarelo(self,steps,spins):
        Mag = []
        for k in tqdm.tqdm(range(steps)):
            i = np.random.randint(M)
            j = np.random.randint(N)
            if j == 0:
                if i == 0:
                    E0 = -self.J * ((spins[i, j] * spins[i, N - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                spins[i, j] * spins[M - 1, j]) + (spins[i, j] * spins[i + 1, j])) - self.B * (
                         spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                                -spins[i, j] * spins[M - 1, j]) + (-spins[i, j] * spins[i + 1, j])) - self.B * (
                             -spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                elif i == M - 1:
                    E0 = -self.J * ((spins[i, j] * spins[i, N - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[i - 1, j]) + (spins[i, j] * spins[0, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                            -spins[i, j] * spins[i - 1, j]) + (-spins[i, j] * spins[0, j])) - self.B * (-spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                else:
                    E0 = -self.J * ((spins[i, j] * spins[i, N - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[i - 1, j]) + (spins[i, j] * spins[i + 1, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                            -spins[i, j] * spins[i - 1, j]) + (-spins[i, j] * spins[i + 1, j])) - self.B * (
                             -spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
            elif j == N - 1:
                if i == 0:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, 0]) + (
                                spins[i, j] * spins[M - 1, j]) + (spins[i, j] * spins[i + 1, j])) - self.B * (
                         spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                            spins[i, j] * spins[M - 1, j]) + (-spins[i, j] * spins[i + 1, j])) - self.B * (-spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                elif i == M - 1:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, 0]) + (
                            spins[i, j] * spins[0, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                            -spins[i, j] * spins[0, j]) + (-spins[i, j] * spins[i - 1, j])) - self.B * (-spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                else:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, 0]) + (
                            spins[i, j] * spins[i + 1, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                            -spins[i, j] * spins[i + 1, j]) + (-spins[i, j] * spins[i - 1, j])) - self.B * (
                             -spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)

            else:
                if i == 0:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                spins[i, j] * spins[i + 1, j]) + (spins[i, j] * spins[M - 1, j])) - self.B * (
                         spins[i, j])
                    E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                            -spins[i, j] * spins[i + 1, j]) + (-spins[i, j] * spins[M - 1, j])) - self.B * (
                             -spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                if i == M - 1:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[0, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[0, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (-spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
                else:
                    E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[i + 1, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (spins[i, j])
                    E1 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                            spins[i, j] * spins[i + 1, j]) + (spins[i, j] * spins[i - 1, j])) - self.B * (-spins[i, j])
                    deltaE = 2 * -spins[i, j] * (E1 - E0)
            if deltaE < 0: #or np.random.rand() < np.exp((- deltaE / k + 1)):
                spins[i, j] = -spins[i, j]
            Mag.append(np.sum(spins) / (M * N))
        return spins, Mag
    """
    def iterate(self,steps, spins):
        Mag = []
        for k in tqdm.tqdm(range(steps)):
            for i in range(M):  # losowanie zadanej liczby spinów
                for j in range(N):
                    if j == 0:
                        if i == 0:
                            E0 = -self.J *((spins[i, j] * spins[i, N-1]) + (spins[i, j] * spins[i, j+1])+(spins[i,j]*spins[M-1,j])+(spins[i,j]*spins[i+1,j])) - self.B*(spins[i,j])
                            E1 = -self.J *((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (-spins[i, j] * spins[M - 1, j]) + (-spins[i, j] * spins[i + 1, j])) -self.B* (-spins[i,j])
                            deltaE = 2 * -spins[i,j] * (E1 - E0)
                        elif i == M-1:
                            E0 = -self.J *((spins[i, j] * spins[i, N - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                        spins[i, j] * spins[i-1, j]) + (spins[i, j] * spins[0, j])) - self.B*(spins[i,j])
                            E1 = -self.J *((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                                    -spins[i, j] * spins[i - 1, j]) + (-spins[i, j] * spins[0, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                        else:
                            E0 = -self.J *((spins[i, j] * spins[i, N-1]) + (spins[i, j] * spins[i, j + 1]) + (
                                    spins[i, j] * spins[i - 1, j]) + (spins[i, j] * spins[i+1, j])) - self.B*(spins[i,j])
                            E1 = -self.J *((-spins[i, j] * spins[i, N - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                                    -spins[i, j] * spins[i - 1, j]) + (-spins[i, j] * spins[i + 1, j])) -self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                    elif j == N-1:
                        if i == 0:
                            E0 = -self.J * ((spins[i,j]*spins[i,j-1])+(spins[i,j]*spins[i,0])+(spins[i,j]*spins[M-1,j])+(spins[i,j]*spins[i+1,j])) - self.B*(spins[i,j])
                            E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                                        spins[i, j] * spins[M - 1, j]) + (-spins[i, j] * spins[i + 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                        elif i==M-1:
                            E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, 0]) + (
                                        spins[i, j] * spins[0, j]) + (spins[i, j] * spins[i -1 , j]))- self.B*(spins[i,j])
                            E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                                    -spins[i, j] * spins[0, j]) + (-spins[i, j] * spins[i - 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                        else:
                            E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, 0]) + (
                                    spins[i, j] * spins[i+1, j]) + (spins[i, j] * spins[i - 1, j])) -  self.B*(spins[i,j])
                            E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, 0]) + (
                                    -spins[i, j] * spins[i + 1, j]) + (-spins[i, j] * spins[i - 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)

                    else:
                        if i ==0:
                            E0 = -self.J * ((spins[i, j] * spins[i, j-1])+(spins[i,j]*spins[i,j+1])+(spins[i,j]*spins[i+1,j])+(spins[i,j]*spins[M-1,j])) - self.B*(spins[i,j])
                            E1 = -self.J * ((-spins[i, j] * spins[i, j - 1]) + (-spins[i, j] * spins[i, j + 1]) + (
                                        -spins[i, j] * spins[i + 1,j]) + (-spins[i, j] * spins[M - 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                        if i == M-1:
                            E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                        spins[i, j] * spins[0,j]) + (spins[i, j] * spins[i-1, j])) - self.B*(spins[i,j])
                            E1 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                    spins[i, j] * spins[0, j]) + (spins[i, j] * spins[i - 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                        else:
                            E0 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                    spins[i, j] * spins[i+1, j]) + (spins[i, j] * spins[i - 1, j])) - self.B*(spins[i,j])
                            E1 = -self.J * ((spins[i, j] * spins[i, j - 1]) + (spins[i, j] * spins[i, j + 1]) + (
                                    spins[i, j] * spins[i + 1, j]) + (spins[i, j] * spins[i - 1, j])) - self.B*(-spins[i,j])
                            deltaE = 2 * -spins[i, j] * (E1 - E0)
                if deltaE<=0 or np.random.rand() < np.exp((- deltaE/k+1)):
                    spins[i,j] = -spins[i,j]
            print(spins)
            Mag.append(np.sum(spins)/(M*N))
        return spins, Mag
"""
B = 1
Beta = 0.00001
J = (-1/2)
M = 9
N = 9
steps = 1000
file = '/Users/adamignaciuk/PycharmProjects/PythonwZastosowaniachNaukowych/Lab2/img.png'
spins = np.zeros((M,N), dtype = int)
Mag = np.zeros(M)


stepsforplot = []
spinsforplot = []

a = IsingModel(J=J,M=M, N=N, B=B, Beta=Beta)
aha = a.randomspins(M,N)
print(aha)

xd,Mag = a.MonteCarelo(steps,aha)
print(xd)




stepsforplot = range(0,steps)
plt.plot(stepsforplot,Mag)
plt.xlabel("Step[n.o]")
plt.ylabel("Sum[a.u.]")
plt.show()




