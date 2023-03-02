import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

usetex = True

def honeycomb():
    f = plt.figure(figsize=(10,10))
    plt.rcParams.update({
        "text.usetex": usetex
    })
    plt.xlim([0,800])
    plt.ylim([0,400])
    ax = f.axes[0]
    ax.set_aspect('equal')

    a = 100
    b = a/np.sqrt(3)

    a1 = a*np.array([3,np.sqrt(3)])/2/np.sqrt(3)
    a2 = a*np.array([3,-np.sqrt(3)])/2/np.sqrt(3)

    firstx = -30
    firsty = 150

    i_ = np.arange(-5,10)
    j_ = np.arange(-5,10)
    i_,j_ = np.meshgrid(i_,j_)
    x_= firstx + a1[0]*i_ +  a2[0]*j_
    y_= firsty + a1[1]*i_ +  a2[1]*j_
    x2_= x_+ b*np.cos(np.pi/3)
    y2_= y_ +b*np.sin(np.pi/3)


    plt.scatter(x_,y_)
    plt.scatter(x2_,y2_)


    rect = patches.Rectangle((a*1.15, 2.27*a), 3*b, a, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    ax.text(180, 330, 'cell_width')
    ax.text(290, 250, 'cell_height',rotation=90)
    ax.text(125, 250, '1')
    ax.text(180, 300, '2')
    ax.text(235, 300, '3')
    ax.text(270, 250, '4')
    ax.text(130, 350, '5')
    ax.text(235, 350, '6')

    ax.text(370, 205, '$b$')
    plt.annotate(text='', xy=(350,200), xytext=(350+b-7,200), arrowprops=dict(arrowstyle='<->'))
    primvec_start = (550,200)
    ax.text(560, 265, '$\mathbf{a_1}=(\sqrt{3}/2,1/2)a$')
    ax.text(560, 125, '$\mathbf{a_2}=(\sqrt{3}/2,-1/2)a$')
    plt.annotate(text='', xy=primvec_start, xytext=tuple(np.array(primvec_start)+np.array(a1)), arrowprops=dict(arrowstyle='<-'))
    plt.annotate(text='', xy=primvec_start, xytext=tuple(np.array(primvec_start)+np.array(a2)), arrowprops=dict(arrowstyle='<-'))
    plt.title('Locations of Gaussians in the bulk of honeycomb lattice')
    # plt.axis('off')
    plt.show()
    plt.rcParams.update({
        "text.usetex": False
    })
