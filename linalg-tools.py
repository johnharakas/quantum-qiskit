"""
This is just some stuff to help when doing some computations.
Its not really intended for plotting since most of them time the result
of applying some operator has complex parts.

I'd check out QuTiP for plotting on the Bloch sphere.
"""
import matplotlib

try:
    matplotlib.use('Qt5Agg')
except ValueError as e:
    print('Error: matplotlib backend\n', e)
    print('Trying:', matplotlib.get_backend())
    matplotlib.use(matplotlib.get_backend())
finally:
    import matplotlib.pyplot as plt

import numpy as np
from numpy import linalg as la

"""
Some quantum gate matrices
Since each is numpy matrix, the adjoint for some operator P is P.H : 
"""

# One, two and three parameter unitary operators
U3 = lambda theta, phi, rho: np.mat([[np.cos(theta / 2), -np.exp(1j * rho) * np.sin(theta / 2)],
                                     [np.exp(1j * phi) * np.sin(theta / 2),
                                      np.exp(1j * rho + 1j * phi) * np.cos(theta / 2)]])
U2 = lambda phi, rho: U3(np.pi / 2, phi, rho)
U1 = lambda rho: U3(0, 0, rho)

# Rotation gates (x,y,z)
Rx = lambda theta: U3(theta, -np.pi / 2, np.pi / 2)
Ry = lambda theta: U3(theta, 0, 0)
Rz = lambda phi: U1(phi)

"""
X: NOT (bit flip)
Z: Phase flip
Y: Bit and phase flip
H: Hadamard gate 
S: sqrt(Z), pi/2 phase rotation
T: pi/4 phase rotation 
"""
X = U3(np.pi, 0, np.pi)
Y = U3(np.pi, np.pi / 2, np.pi / 2)
Z = U1(np.pi)
H = U2(0, np.pi)
S = U1(np.pi / 2)
T = U1(np.pi / 4)

# Controlled-NOT gate
CNOT = np.mat([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 1, 0]])


# ===== simple example, put basis vectors in superpositon and plot(2d)
fig, ax = plt.subplots()
hw, hl = 0.1, 0.1

# ground and excited states |0> and |1>
ket0 = np.mat('1;0')
ket1 = np.mat('0;1')

# Superpositons |+> and |->
b1 = np.real(H * ket0)
b2 = np.real(H * ket1)


# Plot some vectors
k0 = ax.arrow(0, 0, ket0[0, 0], ket0[1, 0],
              fc='C0', ec='C0', alpha=1, linestyle='-', head_width=hw, head_length=hl,
              label="$\\vert 0 \\rangle $")

h0 = ax.arrow(0, 0, b1[0, 0], b1[1, 0],
              fc='C0', ec='C0', alpha=0.5, linestyle='-', head_width=hw, head_length=hl,
              label="$\\vert + \\rangle $")

k1 = ax.arrow(0, 0, ket1[0, 0], ket1[1, 0],
              fc='C1', ec='C1', alpha=1, linestyle='-', head_width=hw, head_length=hl,
              label="$\\vert 1 \\rangle $")

h1 = ax.arrow(0, 0, b2[0, 0], b2[1, 0],
              fc='C1', ec='C1', alpha=0.5, linestyle='-', head_width=hw, head_length=hl,
              label="$\\vert - \\rangle $")

ax.legend(handles=[k0, k1, h0, h1],
          bbox_to_anchor=(1.05, 1),
          loc=2,
          borderaxespad=0)

ax.axhline(color='k', alpha=0.2)
ax.axvline(color='k', alpha=0.2)
s = 1.2
ax.axis([-s, s, -s, s])
ax.set_aspect('equal')
plt.show()