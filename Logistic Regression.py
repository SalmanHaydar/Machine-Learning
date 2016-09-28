# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:13:05 2016

@author: salman
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
import math
style.use("fivethirtyeight")

def sigmoid(theta,z):
    s = 1 / (1 + math.exp(np.dot(theta,z.reshape(len(theta),1))*(-1)))
    return s

def derivative(theta,x,y,j):
    g = np.sum( ((sigmoid(theta,x[i,:]) - y[i,0]) * x[i,j]) for i in range(len(x)) )
    g = g/len(x)
    return g

def cost_func(theta,x,y):
    a = np.sum( ((y[i,0]*math.log(sigmoid(theta,x[i,:]))) + ((1-y[i,0])*math.log(1-sigmoid(theta,x[i,:])))) for i in range(len(x)) )
    c = ( a * (-1) ) / len(x)
    return  c

def gradient_descent_algo(x,y,alpha=0.1,ep=0.0001,max_iter=10000):
    theta = np.ones(len(x[0]))
    temp = np.zeros(len(x[0]))
    jj = cost_func(theta,x,y)
    it = 0
    jit=[]
    jval=[]
    converge = False
    jit.append(it)
    jval.append(jj)
    
    while not converge:
        
        for j in range(len(theta)):
            
            temp[j] = theta[j] - ( alpha * derivative(theta,x,y,j) )
        theta = temp[:]
        temp = np.zeros(len(x[0]))
        jit.append(it)
        jval.append(jj)
        e = cost_func(theta,x,y)
        it = it + 1
        if abs(jj-e)<=ep:
            print("converged at iteration : ",it)
            converge = True
        jj = e
        if it>=max_iter:
            print("Max iteration exeeded!")
            converge= True
    return theta,jit,jval
    
if __name__=="__main__":
    x = [[1,0,0,1,1,1],[1,0,0,1,0,0],[1,0,0,0,1,0],[1,0,1,1,1,1],[1,0,1,0,1,0],[1,1,0,1,1,1],[1,1,0,0,0,0],[1,1,1,1,1,1],[1,1,1,0,0,1],[1,1,0,1,0,0]]
    x = np.array(x)
    y = x[:,-1]
    x = x[:,0:5]
    y = y.reshape(len(x),1)
    x = x.astype(float)
    y = y.astype(float)
    th=[]
    jit=[]
    jval=[]
    th,jit,jval = gradient_descent_algo(x,y)
    plt.plot(jit,jval)
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.title("Cost VS Iteration")
    plt.show()
    print("Theta :")
    print(th)
    pr = np.array([1,0,0,1,1])
    print(sigmoid(th,pr))