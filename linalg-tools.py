'''
Just some plotting stuff for visualizing vectors and matrices. Needs to be organized.
'''

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as la


def plot_basis(H,label=''):
    fig, ax = plt.subplots()
    hw, hl = 0.1,0.1
    bx, by = np.array([1,0]), np.array([0,1])
    stdx = ax.arrow(0, 0,
                    bx[0], bx[1],
                    fc='gray',
                    ec='gray',
                    linestyle='-',
                    head_width=hw,
                    head_length=hl,
                    zorder=1,
                    label="Standard"
                    )
    stdy = ax.arrow(0, 0,
                    by[0], by[1],
                    fc='gray',
                    ec='gray',
                    linestyle='-',
                    head_width=hw,
                    head_length=hl,
                    zorder=1,
                    label="Standard"
                    )

    h1 = ax.arrow(0, 0,
                H[0, 0], H[1, 0],
                fc='k',
                ec='k',
                linestyle='-',
                head_width=hw,
                head_length=hl,
                zorder=1,
                label=label
                )

    h2 = ax.arrow(0, 0,
             H[0, 1], H[1, 1],
             fc='k',
             ec='k',
             linestyle='-',
             head_width=hw,
             head_length=hl,
             zorder=1
             )
    ax.legend(handles=[stdx,h1],bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=1)
    ax.axhline(color='k', alpha=0.2,zorder=0)
    ax.axvline(color='k', alpha=0.2,zorder=0)
    ax.axis([-2, 2, -2, 2])
    ax.set_aspect('equal')

    # plt.title("Basis Vectors")
    # plt.show()




H = np.mat('1 1; 1 -1')/np.sqrt(2)
A = (1/2) * np.matrix('3 1; 1 3')
x = np.matrix('1; 1') / (2 * np.sqrt(2))
b = np.matrix('1; 1') / np.sqrt(2)

# plot_basis(H,"Hadamard")
# plot_basis(A)

fig, ax = plt.subplots()
hw,hl = 0.1,0.1
l, E = la.eig(A)
U = lambda x: A*x

pE=ax.arrow(0, 0, E[0,0], E[1,0], fc='k', ec='k', linestyle=':', head_width=hw, head_length=hl)

pA0 = ax.arrow(0, 0, A[0,0], A[1,0],
               fc='C1', ec='C1', linestyle='-', head_width=hw, head_length=hl, zorder=0, label="Vectors of $A$")
pA1 = ax.arrow(0, 0, A[0,1], A[1,1],
               fc='C1', ec='C1', linestyle='-', head_width=hw, head_length=hl, zorder=0, label="Vectors of $A$")


px=ax.arrow(0,0, x[0,0], x[1,0],
            ec='red', fc='red', alpha=1, linestyle='-', head_width=hw, head_length=hl, zorder=2, label="$\\vert x \\rangle $")

pb=ax.arrow(0,0,
         b[0,0], b[1,0],
         fc='b',
         ec='b',
         # alpha=0.5,
         linestyle='-',
         head_width=hw,
         head_length=hl,
         zorder=1,
         label="A$\\vert x \\rangle $"

         )



ax.axhline(color='k',alpha=0.2)
ax.axvline(color='k',alpha=0.2)
s = 1.75
ax.axis([-s,s,-0.5,s])
ax.set_aspect('equal')
# ax.legend(handles=[pA1,pE,pb,px],
#           bbox_to_anchor=(1.05, 1),
#           loc=2,
#           borderaxespad=0
#           )

plt.show()
