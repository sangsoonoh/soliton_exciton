import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

def colvec(lst):
    return np.transpose(np.array([lst]))

def pillar(x,y,xm,ym):
    p=8
    d=.5
    return -p*np.exp(-((x-xm)**2+(y-ym)**2)/d**2)

def R(x,y):
    a=1.4
    a1 = colvec([np.sqrt(3)*a,0])
    a2 = colvec([np.sqrt(3)*a/2,3*a/2])
    print(np.array([a1,a2]))
    ij = np.linalg.inv(np.array([a1,a2]))*colvec([x,y])
    #let i,j be coords in a1,a2 basis, then:
#     i =
    xm=0
    ym=0
    return pillar(x,y,xm,ym)
   
   
   

x_ = np.arange(-5, 5, 0.25)
y_ = np.arange(-5, 5, 0.25)
x_, y_ = np.meshgrid(x_, y_)
r_ = R(x_,y_)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(x_, y_, r_, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
