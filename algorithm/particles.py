import numpy as np
OMEGA = 4
R1 = 0
R2 = 2
C1 = 1
C2 = 3

class Particle:
    def __init__(self, x, y, r1, c1, r2, c2, omega, f):
        self.variables = (r1, c1, r2, c2, omega)

        self.position = np.array([x, y])
        self.personal_best = self.position
        self.richtungsvector = np.array([0, 0])
        self.f = f

        self.pers_best_list = [self.personal_best]
        self.vec_list = [[0, 0]]
        self.pos_list = [self.position]
        self.comp_list = []
        self.global_best_lst = []

    def move(self, global_best):
        comp1 = self.variables[OMEGA] *  self.richtungsvector
        comp2 = self.variables[C1] * self.variables[R1] * (self.personal_best - self.position)
        comp3 = self.variables[C2] * self.variables[R2] * (global_best - self.position)

        # comp1 = self.richtungsvector
        # comp2 = (self.personal_best - self.position)
        # comp3 = (global_best - self.position)

        self.richtungsvector = self.variables[OMEGA] * self.richtungsvector +\
                               self.variables[C1] * self.variables[R1] * (self.personal_best - self.position) + \
                               self.variables[C2] * self.variables[R2] * (global_best - self.position)

        self.position = self.position + self.richtungsvector

        self.vec_list.append(self.richtungsvector)
        self.pos_list.append(self.position)
        self.global_best_lst.append(global_best)
        self.comp_list.append((comp1, comp2, comp3))

        self.update_personal_best()

    def update_personal_best(self):
        if self.f(*self.personal_best) > self.f(*self.position):
            self.personal_best = self.position
            self.pers_best_list.append(self.personal_best)

    def __str__(self):
        return f'x: {self.position[0]} y: {self.position[1]}, z: {self.f(*self.position)}'

if __name__ == '__main__':
    p = Particle(0, 0, 0.5, 2, 0.5, 2, 0.8, lambda x, y: x+y)
    p.move((0, 0))
    print(p)
