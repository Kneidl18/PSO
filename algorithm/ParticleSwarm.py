import sys

import graph
import particles

import numpy as np
import random

random.seed(10)

class ParticleSwarm:
    particle_list = []
    global_best = np.array([0,0,sys.float_info.max])
    glob_best_list = [global_best]

    def __init__(self, f, x_min, x_max, y_min, y_max, amount: int =10):
        self.f = f
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        for i in range(amount):
            x, y, z = self.calc_rand_position_in_function()
            r1, c1, r2, c2, omega = [random.random() for _ in range(5)]
            c1 = 2
            c2 = 2
            omega = 0.9
            particle = particles.Particle(x, y, r1, c1, r2, c2, omega, self.f)

            self.particle_list.append(particle)

        self.update_global_best()

    def calc_rand_position_in_function(self) -> np.array:
        x = random.uniform(self.x_min+0.3, self.x_max-0.3)
        y = random.uniform(self.y_min+0.3, self.y_max-0.3)
        return np.array([x, y, self.f(x, y)])

    def update_global_best(self):
        for particle in self.particle_list:
            if self.f(*particle.position) < self.global_best[2]:
                # print(str(self.f(*particle.position)) + " < " + str(self.global_best[2]))
                self.global_best = np.array([*particle.position, self.f(*particle.position)])
                self.glob_best_list.append(self.global_best)

    def move(self):
        for paricle in self.particle_list:
            paricle.move(self.global_best[0:2])

        self.update_global_best()

    def __str__(self):
        ret = ''

        for i, particle in enumerate(self.particle_list):
            ret += f'particle {i}: {particle.position}\n'

        return ret



if __name__ == '__main__':
    min_x = -6
    max_x = 4
    min_y = -6
    max_y = 4


    def f(x, y):
        return x**2 + (y + 1)**2 - 5 * np.cos(1.5 * x + 1.5) #- 3 * np.cos(2 * y - 1.5)

    # Create a meshgrid for x and y
    x = np.linspace(min_x-1, max_x+1, 1000)
    y = np.linspace(min_y-1, max_y+1, 1000)
    X, Y = np.meshgrid(x, y)

    # Compute the function values
    Z = f(X, Y)
    g = graph.PlotParticles(X, Y, Z, 1)


    swarm = ParticleSwarm(f, min_x, max_x, min_y, max_y, 5)

    # global_best = swarm.global_best
    # i = 0
    # while i < 5:
    #     swarm.move()
    #     if (global_best == swarm.global_best).all():
    #         i += 1
    #     else:
    #         global_best = swarm.global_best
    #         i = 0

    # amount = 70
    # for i in range(amount):
    #     swarm.move()
    #
    #     if i % (amount//10) != 0:
    #         continue

    for i in range(2):
        swarm.move()

    # for particle in swarm.particle_list:
    #     pos = np.array([*particle.position, f(*particle.position)])
    #     vec = particle.richtungsvector
    #     g.addPoint(*pos)
        #g.addArrow(*(pos-[*vec, 0]), *pos, 'blue')

    index = 2
    g.addPoint(*swarm.particle_list[index].position, f(*swarm.particle_list[index].position), 'black')
    g.addPoint(*swarm.global_best, color='red')
    g.addPoint(*swarm.particle_list[index].personal_best, f(*swarm.particle_list[index].personal_best), 'yellow')
    print(swarm.particle_list[index].position)
    print(swarm.particle_list[index].personal_best)
    print(swarm.particle_list[index].richtungsvector)

        # g.save(i, './plots')
        # g.clear()

    g.plot()
