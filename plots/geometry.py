import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import seaborn as sns

def line(x,y=[0,0],mode='line'):
    
    '''
    USE:    geo([2,10]) 
   
    '''
    sns.set_context('notebook')
    plt.style.use('seaborn-bright')

    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    line = Line2D(x, y)
    ax.add_line(line)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    plt.grid(b=True, which='major', color='grey', linestyle='--')
    plt.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
    plt.minorticks_on()
    plt.show()

    plt.show()
    
def poly(xyz):
    
    '''
    USE: poly([[2,8],[1,3],[4,5]])
    '''
    
    fig, ax = plt.subplots()
    patches = []

    polygon = Polygon(xyz, True)
    patches.append(polygon)

    p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)

    colors = 100*np.random.rand(len(patches))
    p.set_array(np.array(colors))
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    ax.add_collection(p)

    plt.show()
