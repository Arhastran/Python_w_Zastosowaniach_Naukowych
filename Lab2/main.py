#Adam Ignaciuk Python w zastosowaniach naukowych laboratorium drugie

#Ising model in 2D with Monte Carlo algorithm

import numpy as np
import random as random
import tqdm
import matplotlib.pyplot as plt

class IsingModel:
    def __init__(self , spin = 0, M = 1, N=1 , B = 1, Beta= 1, J = 1):
        self.spins = self
        self.spin = self

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


B = 1
Beta = 0.00001
J = 0.35
M = 20
N = 10
steps = 1

stepsforplot = []
spinsforplot = []

a = IsingModel()
aha = a.randomspins(M,N)


for i in tqdm.tqdm(range(M)):
    for j in range(N):
        E0 = a.hamiltonian(J,aha) - B*aha[i,j]
        aha[i,j] = -aha[i,j]
        E1 = a.hamiltonian(J,aha) - B*aha[i,j]
        deltaE = E1-E0
        if deltaE < 0:
            pass
        elif deltaE > 0:
            pos = a.possibility(Beta,deltaE)
            aha[i, j] = -aha[i, j]
        else:
            pass
        spinsforplot.append(np.sum(aha)/(M*N))

stepsforplot = range(0,M*N)
plt.plot(stepsforplot,spinsforplot)
plt.xlabel("Step[n.o]")
plt.ylabel("Sum[a.u.]")
plt.show()



