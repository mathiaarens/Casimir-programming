
import matplotlib as mat
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.axes()

def circleplot(radius):
    circle = plt.Circle((0,0),radius, fc='y')    
    plt.gca().add_patch(circle)
    plt.savefig('circle.png')
    plt.show()
    
#plt.axis('scaled')
    
circleplot(1)

