"""
Created at 24.10.2019
"""

import numpy as np

# TODO QUASIRANDOM & GRID
#  http://ww2.ii.uj.edu.pl/~arabas/workshop_2019/files/talk_Shima.pdf


class Pseudorandom:

    @staticmethod
    def sample(grid, n_sd):
        dimension = len(grid)
        positions = np.random.rand(dimension, n_sd)
        for dim in range(dimension):
            positions[dim, :] *= grid[dim]
        return positions
