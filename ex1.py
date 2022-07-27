import math
import numpy as np

iteration = 0
epsilon = 10 ** -6

def f(x):
    return 3 * x + np.sin(x) - np.exp(x)                                                  #the function


def algoritem(a, b):
    c = (a + b) / 2
    iteration = 0
    while (abs(f(c)) > epsilon):
        c = (a + b) / 2
        iteration = iteration + 1
        k = f(c)
        if (k * f(a) < 0):
            b = c
        else:
            a = c
        print(f"the numbers of iterations is: {iteration}")
        print(f"c = {c}")
        print(f"the norma is:{abs(k)}")


algoritem(0, 1)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def function1_result(x, y, z):                                          #
    a = z ** 2 - x * y + 1
    b = x ** 2 - x * y * z - y ** 2 + 2
    c = -1*np.exp(x) + np.exp(y) -z + 3
    d = np.array([a,b,c])
    return d


def arrayOfDeter(x, y, z):                                               #jacob
    return ([[-x, -y, 2 * z],
             [2 * x - y * z, -2 * y - x * z, -x * y],
             [-1 *math.e ** x, math.e ** y, -1]])



r = function1_result(1,1,1)                                               #the guess
e = abs(r)
max = np.amax(e)                                                          #get the max
x = y = z = 1
while max > epsilon:
    max_result = function1_result(x,y,z)                                  #maxResult- array
    absulutValue = abs(max_result)
    max = np.amax(absulutValue)
    deter1 = arrayOfDeter(x,y,z)
    vectorResult = np.linalg.solve(deter1,-max_result)
    x = x + vectorResult[0]                                                #update x
    y = y + vectorResult[1]                                                #update y
    z = z + vectorResult[2]                                                #update z
    res = np.array([x,y,z])                                                #make array with the update details
    print("f(x) = :",res,"norm :",max)



