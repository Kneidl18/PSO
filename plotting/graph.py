from .combine_pdf import combine
from . import defines

import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams["font.sans-serif"] = "helvetica"

class PlotParticles:
    """
    A class to create and manage 3D plots of particles.

    Attributes:
        points (list[plt.plot]): List to store plotted points.
        vectors (list): List to store plotted vectors.
        x_min (int): Minimum x-axis value.
        x_max (int): Maximum x-axis value.
        y_min (int): Minimum y-axis value.
        y_max (int): Maximum y-axis value.
    """
    points: list[plt.plot] = []
    vectors = []

    x_min, x_max = -4, 3
    y_min, y_max = -4, 2

    def __init__(self, x, y, z, setting):
        """
        Initializes the PlotParticles instance with given x, y, z data and setting.

        Args:
            x (array-like): X-axis data.
            y (array-like): Y-axis data.
            z (array-like): Z-axis data.
            setting (int): Plot setting option.
        """
        self.x = x
        self.y = y
        self.z = z
        self.option = setting
        self.setup()

    def setup(self):
        """
        Sets up the 3D plot based on the provided option.
        """
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

        elif self.option == 1:
            self.ax.view_init(elev=45, azim=-45)

            # Create the 3D surface
            self.ax.plot_surface(self.x, self.y, self.z, cmap='coolwarm', edgecolor='none', alpha=0.5)
            self.ax.contourf(self.x, self.y, self.z, zdir='z', levels=80, cmap='coolwarm', alpha=1)

    def addPoint(self, x, y, z, color='black', size=5, trans=1):
        """
        Adds a point to the 3D plot.

        Args:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the arrow start.
            z (float): Z-coordinate of the arrow start.
            u (float): X-component of the arrow vector.
            v (float): Y-component of the arrow vector.
            w (float): Z-component of the arrow vector.
            y (float): Y-coordinate of the point.
            z (float): Z-coordinate of the point.
            color (str, optional): Color of the point. Defaults to 'black'.
            size (int, optional): Size of the point. Defaults to 5.
            trans (float, optional): Transparency of the point. Defaults to 1.
        """
        self.points.append(self.ax.plot(xs=x, ys=y, zs=z, marker='.', color=color, markersize=size, zorder=4, alpha=trans))

    def addArrow(self, x, y, z, u, v, w, color='red'):
        """
        Adds an arrow to the 3D plot.

        Args:
            x (float): X-coordinate of the arrow start.
            color (str, optional): Color of the arrow. Defaults to 'red'.
        """
        self.vectors.append(self.ax.arrow3D(
            x,y,z,u,v,w,
            color=color, fc=color, arrowstyle="-|>", lw=2, mutation_scale=15
        ))

    def plot(self):
        """
        Displays the 3D plot.
        """
        if self.option == defines.SWARM:
            self.ax.axis('off')
        elif self.option == defines.INTRO:
            self.ax.set_xlim(self.x_min, self.x_max)
            self.ax.set_ylim(self.y_min, self.y_max)
            self.ax.axis('off')

        plt.show()

    def save(self, i, path):
        """
        Saves the 3D plot to a PDF file and combines PDFs if necessary.

        Args:
            i (int): Index for the filename.
            path (str): Directory path to save the PDF.
        """
        def save_plot(filename="pso_fig_" + str(i) + ".pdf"):
            """
            Saves the current plot to a PDF file.

            Args:
                filename (str, optional): Name of the PDF file. Defaults to "pso_fig_" + str(i) + ".pdf".
            """
            if not os.path.exists(path):
                os.makedirs(path)
            filepath = os.path.join(path, filename)
            plt.savefig(filepath, format="pdf")

        if self.option == defines.SWARM:
            self.ax.set_xlim(-7, 5)
            self.ax.set_ylim(-7, 5)
            self.ax.set_zlim(0, 90)
            self.ax.set_yticklabels([])
            self.ax.set_xticklabels([])
            self.ax.set_zticklabels([])

        elif self.option == defines.INTRO:
            self.ax.set_xlim(self.x_min, self.x_max)
            self.ax.set_ylim(self.y_min, self.y_max)
            self.ax.axis('off')

        save_plot()
        combine(self.option)

    def clear(self):
        """
        Clears the current plot and resets the setup.
        """
        plt.clf()
        plt.cla()
        self.setup()