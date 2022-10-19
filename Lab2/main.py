#Adam Ignaciuk Python w zastosowaniach naukowych laboratorium drugie

#Ising model in 2D with Monte Carlo algorithm

import numpy as np
import random as random
#import Pillow as pillow

class RandomSpinGenerator:
    def __init__(self , size = 1, newspins = 0, T = 0, spins = []):
        self.spin = self
        self.newspin = self
    def randomspins(self, size): #random spins web generator
        spinslist = []
        for i in range(size):
            self.spin = random.randint(0, 1)
            if self.spin == 0:
                spinslist.append(-1)
            else:
                spinslist.append(1)
        return (spinslist)

    def statechange(self, spin): #change state of another spin
        newspin = spin*-1
        return newspin

    def energyfunction(self, spins, T):
        sum = np.sum(spins)
        energy = np.exp(-(2*sum)/T)
        return energy

#web parameters
M = 10
N = 10
spins = []


a = RandomSpinGenerator()
spins = a.randomspins(M*N)

print(spins)

for i in range(M*N):
    a = RandomSpinGenerator()
    spins[i] = a.statechange(spins[i])

energy = a.energyfunction(spins,250)

print(spins)
print(energy)


