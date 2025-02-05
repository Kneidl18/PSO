# abortion when 40 times no update of global best

import numpy as np
import matplotlib.pyplot as plt
import arrow
import os

#print(plt.rcParams.keys())
plt.rcParams["font.sans-serif"] = "helvetica"

class PlotParticles:
    points: list[plt.plot] = []
    vectors = []

    x_min, x_max = -4, 3
    y_min, y_max = -4, 2
    def __init__(self, x, y, z, setting):
        self.x = x
        self.y = y
        self.z = z
        self.option = setting
        self.setup()

    def setup(self):
        # Plot the 3D surface plot
        self.fig = plt.figure(figsize=(12, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        if self.option == 0:
            self.ax.view_init(elev=90, azim=0)
            # terrain
            mask = ((self.x >= self.x_min-1) & (self.x <= self.x_max+1) &
                    (self.y >= self.y_min-1) & (self.y <= self.y_max+1))
            z_masked = np.where(mask, self.z, np.nan)
            self.ax.contourf(self.x, self.y, z_masked, zdir='z', levels=50, cmap='coolwarm', alpha=1)
            #self.ax.contourf(self.x, self.y, self.z, zdir='z', levels=80, cmap='coolwarm', alpha=1)

        elif self.option == 1:
            self.ax.view_init(elev=45, azim=-45)

            # Create the 3D surface
            #fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5, label='f(x, y)')
            self.ax.plot_surface(self.x, self.y, self.z, cmap='coolwarm', edgecolor='none', alpha=0.5)
            self.ax.contourf(self.x, self.y, self.z, zdir='z', levels=80, cmap='coolwarm', alpha=1)

    def addPoint(self, x, y, z, color='black', size=5, trans=1):
        # Add the dot at (0, 0, Z)
        self.points.append(self.ax.plot(xs=x, ys=y, zs=z, marker='.', color=color, markersize=size, zorder=4, alpha=trans))

    def addArrow(self, x, y, z, u, v, w, color='red'):
        self.vectors.append(self.ax.arrow3D(
            x,y,z,u,v,w,
            color=color, fc=color, arrowstyle="-|>", lw=2, mutation_scale=15
        ))

    def plot(self):
        if self.option == 1:
            # Labels and title
            # self.ax.set_title("3D Surface Plot of f(x, y)")
            # self.ax.set_xlabel("x")
            # self.ax.set_ylabel("y")
            # self.ax.set_zlabel("f(x, y)")
            self.ax.axis('off')
        elif self.option == 0:
            self.ax.set_xlim(self.x_min, self.x_max)
            self.ax.set_ylim(self.y_min, self.y_max)
            #self.ax.set_xlabel("x")
            #self.ax.set_ylabel("y")
            self.ax.axis('off')

        plt.show()

    def save(self, i, path):
        def save_plot(filename="pso_fig_" + str(i) + ".pdf"):
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = os.path.join(path, filename)
            plt.savefig(filepath, format="pdf")

        if self.option == 1:
            # Labels and title
            # self.ax.set_title("3D Surface Plot of f(x, y)")
            # hfont = {'fontname':'Helvetica'}
            # self.ax.set_xlabel("x", **hfont)
            # self.ax.set_ylabel("y", **hfont)
            # self.ax.set_zlabel("f(x, y)")
            self.ax.set_xlim(-7, 5)
            self.ax.set_ylim(-7, 5)
            self.ax.set_zlim(0, 90)
            self.ax.set_yticklabels([])
            self.ax.set_xticklabels([])
            self.ax.set_zticklabels([])
            #self.ax.axis('off')

        elif self.option == 0:
            self.ax.set_xlim(self.x_min, self.x_max)
            self.ax.set_ylim(self.y_min, self.y_max)
            # self.ax.set_xlabel("x")
            # self.ax.set_ylabel("y")
            self.ax.axis('off')

        save_plot()


    def clear(self):
        plt.clf()
        plt.cla()
        self.setup()



if __name__ == '__main__':
    def f(x, y):
        return x**2 + (y + 1)**2 - 5 * np.cos(1.5 * x + 1.5) #- 3 * np.cos(2 * y - 1.5)

    # Create a meshgrid for x and y
    x = np.linspace(-5, 5, 1000)
    y = np.linspace(-5, 5, 1000)
    X, Y = np.meshgrid(x, y)

    # Compute the function values
    Z = f(X, Y)

    test_point = f(0, 0)

    plotit = PlotParticles(X, Y, Z, 1)
    plotit.addPoint(0, 0, test_point)
    plotit.addArrow(0, 0, 0, 1, 1, 1)
    plotit.plot()