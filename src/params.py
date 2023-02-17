import numpy as np 
import math as m

# gather system parameters
class Params():
	def __init__(self,
					Nx = 9, Ny =1, 
                    nx = 450, ny = 90,
                    a = 1, b = 1/m.sqrt(3),
					a1_norm = np.array([0.5*m.sqrt(3), 0.5]), a2_norm = np.array([0.5*m.sqrt(3), -0.5]), 
					g1 = np.array([0.5, 0.5*m.sqrt(3)]), g2 = np.array([-0.5, 0.5*m.sqrt(3)]), 
					):
		"""
		Init the parameters of the system
		"""
		self.Nx = Nx
		self.Ny = Ny
		self.nx = nx
		self.ny = ny

		self.a = a
		self.b = b

		self.a1 = a*a1_norm
		self.a2 = a*a2_norm
		self.g1 = g1
		self.g2 = g2
    
	def __str__(self):
		str_params = "#####################\n### Params system ###\n#####################\n"
		str_params += f"Domain size (in period a): Nx = {self.Nx}, Ny = {self.Ny}\n"
		str_params += f"Number of grids: nx = {self.nx}, ny = {self.ny}\n"
		str_params += f"periodicity: a = {self.a}, side length = {self.b}\n"
		str_params += f"Lattice vectors: a1 = {self.a1}, a2 = {self.a2}\n"
		str_params += f"Reciprocal lattice vectors: g1 = {self.g1}, g2 = {self.g2}\n"
		return str_params
