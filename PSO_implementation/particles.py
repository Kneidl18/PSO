import numpy as np
OMEGA = 4
R1 = 0
R2 = 2
C1 = 1
C2 = 3

class Particle:
    def __init__(self, x, y, r1, c1, r2, c2, omega, f):
        """
        Initializes a Particle instance with the given parameters.

        Args:
            x (float): Initial x-coordinate of the particle.
            y (float): Initial y-coordinate of the particle.
            r1 (float): Random coefficient 1.
            c1 (float): Cognitive coefficient.
            r2 (float): Random coefficient 2.
            c2 (float): Social coefficient.
            omega (float): Inertia weight.
            f (callable): The function to optimize.
        """
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
        """
        Moves the particle towards its personal best and the global best position.

        Args:
            global_best (np.array): The global best position found by the swarm.
        """
        comp1 = self.variables[OMEGA] *  self.richtungsvector
        comp2 = self.variables[C1] * self.variables[R1] * (self.personal_best - self.position)
        comp3 = self.variables[C2] * self.variables[R2] * (global_best - self.position)

        self.richtungsvector = self.variables[OMEGA] * self.richtungsvector + \
                               self.variables[C1] * self.variables[R1] * (self.personal_best - self.position) + \
                               self.variables[C2] * self.variables[R2] * (global_best - self.position)

        self.position = self.position + self.richtungsvector

        self.vec_list.append(self.richtungsvector)
        self.pos_list.append(self.position)
        self.global_best_lst.append(global_best)
        self.comp_list.append((comp1, comp2, comp3))

        self.update_personal_best()

    def update_personal_best(self):
        """
        Updates the personal best position of the particle.
        """
        if self.f(*self.personal_best) > self.f(*self.position):
            self.personal_best = self.position
            self.pers_best_list.append(self.personal_best)

    def __str__(self):
        """
        Returns a string representation of the particle.

        Returns:
            str: String representation of the particle's position and function value.
        """
        return f'x: {self.position[0]} y: {self.position[1]}, z: {self.f(*self.position)}'

if __name__ == '__main__':
    p = Particle(0, 0, 0.5, 2, 0.5, 2, 0.8, lambda x, y: x+y)
    p.move((0, 0))
    print(p)