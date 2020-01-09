"""
Created at 18.12.2019

@author: Piotr Bartman
@author: Sylwester Arabas
"""


def global_FisherYates(particles, cell_start, u01):
    particles.state.unsort_global(u01, temp=cell_start)
    particles.state.sort_by_cell_id(cell_start)


def local_FisherYates(particles, cell_start, u01):
    particles.state.sort_by_cell_id(cell_start)
    particles.state.unsort_local(u01, cell_start)


def global_Shima(particles, cell_start, u01):

    particles.state.sort_by_cell_id(cell_start)
