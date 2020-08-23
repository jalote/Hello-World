# Generating data sets for trying classification

import numpy
import math
import matplotlib.pyplot as plt

# This generates data which are grouped in two groups - for trying classifcation 
def gen1():
    x_var = numpy.random.uniform(0.0, 0.5, 50)
    x = []
    for i in range(50):
        x.append(round((0.5*i + x_var[i]),2))

    y_var = numpy.random.uniform(0.0, 2.0, 25)
    y1 = []
    for i in range(25):
        y1.append(round((6.0 - i*0.1 + y_var[i]), 2))
    y_var = numpy.random.uniform(0.0, 4.0, 25)
    y2 = []
    for i in range(25):
        y2.append(round((8.0 - i*0.2 + y_var[i]), 2))
    y = y1+y2
    return(x,y)


# Trying a sigmoid function
def sigmoid()

       
(x,y) = gen1()
print ("Values of X. No of elts:", len(x))
print(x)
print ("Values of Y. No of elts: ", len(y))
print(y)

plt.scatter(x,y)
#plt.show()

newY = [(1/(1 + math.exp(-1.0*xval))) for xval in x]
plt.scatter(x, newY)
plt.show()


'''

# Plotting the sigmoid or logistic function
x = numpy.linspace(-10, 10, 100)
z = 1 / (1+numpy.exp(-x))
plt.plot(x,z)
plt.xlabel("X")
plt.ylabel("Sigmoid(X)")
plt.show()

'''

