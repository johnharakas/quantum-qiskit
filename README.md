# quantum-qiskit
Quantum computing scratchpad and recipes for IBM Q

Some [pdf notes](Some%20Notes.pdf) have been uploaded which includes some more granular information. 

A highly useful method of visualization is to see how individual quantum states as vectors lie within a unit sphere.  Check out the juypter notebook for visualization of qubit [states on the bloch sphere](bloch_sphere.ipynb). Essentially all operations can be viewed as rotating and reflecting a vector along those three axes. 

[simple_solver](simple_solver.ipynb) is an implementation of the algorithm to solve systems of linear equations. Although the output has not been clearly explained. 

[linalg_tools](linalg-tools.py) contains the matrix representations of common gates and general unitary operators, mostly just as a helper in computation. 

[testrun](testrun.ipynb) creates what is called a Bell state. This is fundamental for quantum teleportation and has implications in secure key distribution among other things. In that test case, is to check for bit equality. 

[deutsch](deutsch.ipynb) is an example of Deutsch's Algorithm, a simple, but fundamental result. 
