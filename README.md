# PSO

## Overview
This project is an implementation of the Particle Swarm Optimization (PSO) algorithm. PSO is a computational method used for optimizing a problem by iteratively improving a candidate solution with regard to a given measure of quality. This implementation includes the core PSO algorithm, particle movement, and visualization of the optimization process.

## Features
- **Particle Swarm Optimization Algorithm**: Implements the PSO algorithm to find the optimal solution.
- **Visualization**: Uses Matplotlib to create 3D plots of the particles and their movements.
- **PDF Export**: Combines multiple plots into a single PDF file for easy sharing and analysis.

## Requirements
- Python 3.x
- `numpy`
- `matplotlib`
- `PyPDF2`

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/PSO.git
    cd PSO
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Define the function to optimize in `simulate_swarm.py`:
    ```python
    def f(x, y):
        return x**2 + (y + 1)**2 - 5 * np.cos(1.5 * x + 1.5)
    ```
2. Initialize the particle swarm and run the simulation:
    ```python
    swarm = ParticleSwarm(f, min_x, max_x, min_y, max_y, num_particles)
    for i in range(iterations_t):
        swarm.move()
        # how often to plot (here each 10 iterations)
        if i % (amount//10) == 0:
            plot_it()
            save_it()
    ```
3. Run the simulation script:
    ```sh
    python simulate_swarm.py
    ```

## Project Structure
- `PSO_implementation.py`: Contains the `Particle` and `ParticleSwarm` classes implementing the PSO algorithm.
- `plotting/graph.py`: Contains the `PlotParticles` class for visualizing the particles in 3D space.
- `combine_pdf.py`: Contains functions to combine multiple PDF files into one.
- `simulate_swarm.py`: Main script to run the PSO simulation and generate plots.
- `README.md`: Project documentation.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.