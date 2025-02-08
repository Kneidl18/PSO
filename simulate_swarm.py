from PSO_implementation import ParticleSwarm
from plotting import graph
import numpy as np


min_x = -6
max_x = 4
min_y = -6
max_y = 4


# the function
def f(x, y):
    return x**2 + (y + 1)**2 - 5 * np.cos(1.5 * x + 1.5)

# Create a meshgrid for x and y
x = np.linspace(min_x-1, max_x+1, 1000)
y = np.linspace(min_y-1, max_y+1, 1000)
X, Y = np.meshgrid(x, y)

# Compute the function values
Z = f(X, Y)
g = graph.PlotParticles(X, Y, Z, 1)


# init the swarm
swarm = ParticleSwarm(f, min_x, max_x, min_y, max_y, 100)

def plot_it():
    for particle in swarm.particle_list:
        pos = np.array([*particle.position, f(*particle.position)])
        g.addPoint(*pos)
    g.addPoint(*swarm.global_best, color='white')


def save_it():
    g.save(i, './plots/swarm')
    g.clear()


amount = 100
for i in range(amount):
    swarm.move()

    if i % (amount//10) != 0:
        continue

    plot_it()
    save_it()
