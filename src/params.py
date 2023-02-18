import numpy as np 
import math as m

# gather system parameters
class Params():
	def __init__(self,
					Nx = 9, Ny =1, Nkx = 15, Nky= 5,
					Lx = 1.2, Ly = 1,
                    a = 1, b = 1/m.sqrt(3),
					a1_norm = np.array([0.5*m.sqrt(3), 0.5]), a2_norm = np.array([0.5*m.sqrt(3), -0.5]), 
					g1_norm = np.array([0.5, 0.5*m.sqrt(3)]), g2_norm = np.array([-0.5, 0.5*m.sqrt(3)]), 

					dx = 0.05, dy = 0.05
					):
		"""
		Init the parameters of the system
		"""
		self.Nx = Nx
		self.Ny = Ny
		self.Nkx = Nkx
		self.Nky = Nky
		self.Nkx_max = m.floor(Nkx/2)
		self.Nky_max = m.floor(Nky/2)		

		self.a = a
		self.b = b

		self.a1 = a*a1_norm
		self.a2 = a*a2_norm

		self.g1_norm = g1_norm
		self.g2_norm = g2_norm
		self.g1 = 2*m.pi/(a*Lx) *g1_norm
		self.g2 = 2*m.pi/(a*Ly) *g2_norm

		self.G1 = 2*m.pi/(a*Lx)*np.array([1, 0]) 
		self.G2 = 2*m.pi/(a*Ly)*np.array([0, 1])

		self.dx = dx
		self.dy = dy

	def __str__(self):
		str_params = "#####################\n### Params system ###\n#####################\n"
		str_params += f"Domain size (in period a): Nx = {self.Nx}, Ny = {self.Ny}\n"
		str_params += f"Number of plane waves: Nkx = {self.Nkx}, Nky = {self.Nky}\n"
		str_params += f"Nkx_max = {self.Nkx_max}, Nky_max = {self.Nky_max}\n"
		# str_params += f"Number of grids: nx = {self.nx}, ny = {self.ny}\n"
		str_params += f"Period: a = {self.a}, Side length: b = {self.b}\n"
		str_params += f"Lattice vectors: a1 = {self.a1}, a2 = {self.a2}\n"
		str_params += f"Grid size: dx =  {self.dx}, dy = {self.dy}\n"
		str_params += f"Reciprocal lattice vectors: g1 = (2*pi/Lx){self.g1_norm}, g2 = (2*pi/Ly){self.g2_norm}\n"
		return str_params
