# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:13:14 2016

@author: salman
"""
import numpy as np
from sklearn.datasets.samples_generator import make_regression
from matplotlib import pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

def cost(t0,t1,x,y):
    est = [t0+t1*x[i] for i in range(0,len(x))]
    p = np.sum((est[i]-y[i])**2 for i in range(0,len(y)))
    j = p / (2*len(x))
    return j
    
def derivative(t0,t1,x,y):
    grad0 = np.sum((t0 + t1*x[i] - y[i]) for i in range(len(x)))/len(x)
    grad1 = np.sum(((t0 + t1*x[i] - y[i]) * x[i]) for i in range(len(x)))/len(x)
    return grad0,grad1
    
def gradient_descent(x,y,alpha = 0.01,ep = 0.01,max_iter = 1000):
    converge = False
    t0 = 0
    t1 = 0
    it = 1
    j = cost(t0,t1,x,y)
    
    while not converge:
        grad0,grad1 = derivative(t0,t1,x,y)
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1
        
        t0 = temp0
        t1 = temp1
        
        e = cost(t0,t1,x,y)
        
        if abs(j-e)<=ep:
            print("converged!")
            print(it)
            converge = True
        j = e
        
        it = it + 1
        if it>=max_iter:
            print("Max Iterator exceed")
            converge = True
    return t0,t1

if __name__=="__main__":
    #x = [3,1,0,4]
    #y = [2,2,1,3]
    x, y = make_regression(n_samples=100, n_features=1, n_informative=1, random_state=0, noise=35)
    t0,t1 = gradient_descent(x,y)
    plt.scatter(x,y)
    ls = [(t0+t1*x[i]) for i in range(len(x))]
    plt.plot(x,ls)
    plt.show()
    print(t0)
    print(t1)