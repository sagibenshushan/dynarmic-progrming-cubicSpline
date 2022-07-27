

from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt 
import numpy as np
def yy(x):
    return 1 / (1 + 12 * x ** 2)


if __name__ == "__main__":
    x = [-5, -2.5, 0, 2.5, 5]         
    # array of x's point that show definition area
    y = [yy(x[0]),yy(x[1]),yy(x[2]),yy(x[3]) ,yy(x[4])]
    # f(x)
    plt.plot(x, y, color='red', linewidth = 3,label='function',marker = 'o', linestyle='dotted', markerfacecolor='black', markersize=11)

    z1 = 0
    z5 = 0
    z2 = 0.403
    z4 = 0.403
    z3 = -0.675
    z = [z1, z2, z3, z4, z5]
    # array of z
    
    F12 = lambda X: (z1 / 6) * ((((X - x[1]) ** 3) / (x[0] - x[1])) - ((X - x[1]) * (x[0] - x[1]))) - (z[1] / 6) * (((((X - x[0]) ** 3) / (x[0] - x[1]))) - ((X - x[0]) * (x[0] - x[1]))) + ((y[0] * (X - x[1])) - (y[1] * (X - x[0]))) / (x[0] - x[1]) 
    # the function between x = 1 to x = 2 
    F23 = lambda X: (z2 / 6) * ((((X - x[2]) ** 3) / (x[1] - x[2])) - ((X - x[2]) * (x[1] - x[2]))) - (z[2] / 6) * (((((X - x[1]) ** 3) / (x[1] - x[2]))) - ((X - x[1]) * (x[1] - x[2]))) + ((y[1] * (X - x[2])) - (y[2] * (X - x[1]))) / (x[1] - x[2])  
    # the function between x = 2 to x = 3 
    F34 = lambda X: (z3 / 6) * ((((X - x[3]) ** 3) / (x[2] - x[3])) - ((X - x[3]) * (x[2] - x[3]))) - (z[3] / 6) * (((((X - x[2]) ** 3) / (x[2] - x[3]))) - ((X - x[2]) * (x[2] - x[3]))) + ((y[2] * (X - x[3])) - (y[3] * (X - x[2]))) / (x[2] - x[3])
    # the function between x = 3 to x = 4 
    F45 = lambda X: (z4 / 6) * ((((X - x[4]) ** 3) / (x[3] - x[4])) - ((X - x[4]) * (x[3] - x[4]))) - (z[4] / 6) * (((((X - x[3]) ** 3) / (x[3] - x[4]))) - ((X - x[3]) * (x[3] - x[4]))) + ((y[3] * (X - x[4])) - (y[4] * (X - x[3]))) / (x[3] - x[4])
    # the function between x = 4 to x = 5 

    X1 = np.linspace(-5,-2.5)
    # the definition area of X1
    X2 = np.linspace(-2.5,0)
    # the definition area of X2
    X3 = np.linspace(0,2.5)
    # the definition area of X3
    X4 = np.linspace(2.5,5)
    # the definition area of X4

    plt.plot(X1,F12(X1),'black')
    # show the function in X1 definition area in color balck
    plt.plot(X2,F23(X2),'blue')
    # show the function in X2 definition area in color blue
    plt.plot(X3,F34(X3),'yellow')
    # show the function in X3 definition area in color yellow
    plt.plot(X4,F45(X4),'red')
    # show the function in X4 definition area in color red
    plt.legend()
    plt.show()
    # function that show the graph