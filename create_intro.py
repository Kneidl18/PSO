from ParticleSwarm import ParticleSwarm
import graph
import numpy as np


min_x = -6
max_x = 4
min_y = -6
max_y = 3


def f(x, y):
    return x**2 + (y + 1)**2 - 5 * np.cos(1.5 * x + 1.5)

# Create a meshgrid for x and y
x = np.linspace(min_x-1, max_x+1, 1000)
y = np.linspace(min_y-1, max_y+1, 1000)
X, Y = np.meshgrid(x, y)

# Compute the function values
Z = f(X, Y)
g = graph.PlotParticles(X, Y, Z, 0)


swarm = ParticleSwarm(f, min_x, max_x, min_y, max_y, 10)

index = 1
pos = 2
run_it = 3
for i in range(run_it):
    swarm.move()

# g.addPoint(*swarm.particle_list[index].position, f(*swarm.particle_list[index].position), 'black')
# point = swarm.particle_list[index].position
# if i > 0:
#     last_vec = swarm.particle_list[index].vec_list[i-1]
#     g.addArrow(*(point - last_vec), f(*(point - last_vec)), *point, f(*point))
#     # g.addArrow(*point, f(*point), *last_vec, f(*last_vec))
# g.addPoint(*swarm.particle_list[index].position, f(*swarm.particle_list[index].position), 'black')

positions =swarm.particle_list[index].pos_list
vecs =swarm.particle_list[index].vec_list
p_best =swarm.particle_list[index].pers_best_list
vec_update =swarm.particle_list[index].comp_list
glob_best = [*swarm.particle_list[index].global_best_lst[pos], f(*swarm.particle_list[index].global_best_lst[pos])]

# for i, pos in enumerate(positions):
#     #g.addPoint(*pos, f(*pos), 'black')
#     if i+1 < len(vecs):
#         continue
#         g.addArrow(*pos, f(*pos), *vecs[i+1], f(*vecs[i+1]))

vec = vec_update[pos][0] + vec_update[pos][1] + vec_update[pos][2]
# g.addPoint(*swarm.glob_best_list[4], color='white')
# g.addPoint(*positions[2], f(*positions[2]), 'black')
# g.addPoint(-0.848, -1, f(-0.848, -1), 'red')
# g.addPoint(*swarm.particle_list[index].personal_best, f(*swarm.particle_list[index].personal_best), 'yellow')

position = np.array([*positions[pos], f(*positions[pos])])

color = ['black', 'firebrick']
arrows = [lambda func, col: func.addArrow(*positions[pos], f(*positions[pos]), *vec_update[pos][0], f(*vec_update[pos][0])+f(*positions[pos]), col),
            lambda func, col: func.addArrow(*positions[pos], f(*positions[pos]), *vec_update[pos][1], f(*vec_update[pos][1])-f(*positions[pos]), col),
            lambda func, col: func.addArrow(*positions[pos], f(*positions[pos]), *vec_update[pos][2], f(*(vec_update[pos][2]+position[:2]))-position[2], col),
            lambda func: func.addArrow(*positions[pos], f(*positions[pos]), *vec, f(*(vec+position[:2]))-position[2], 'firebrick')]

for i in range(-1, len(arrows)):
    mark_size = 20
    g.addPoint(*glob_best, 'white', size=mark_size)
    g.addPoint(*positions[2], f(*positions[2]), 'black', size=mark_size)
    g.addPoint(-0.848, -1, f(-0.848, -1), 'yellowgreen', size=mark_size)
    g.addPoint(*swarm.particle_list[index].personal_best, f(*swarm.particle_list[index].personal_best), 'orange', size=mark_size)

    for j in range(i+1):
        if j == len(arrows) - 1:
            arrows[j](g)
        elif j == i:
            arrows[j](g, color[1])
        else:
            arrows[j](g, color[0])

    g.save(i+1, './plots/intro')
    g.clear()

#g.plot()
