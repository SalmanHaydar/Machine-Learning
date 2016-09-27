# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:01:54 2016

@author: salman
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

def cost(theta,x,y):
    a = np.dot(theta,x.transpose())
    p = np.sum((a-y.transpose())**2)
    j = p/(2*len(x))
    return j

def derivative(theta,x,y,j):
    a = np.dot(theta,x.transpose())
    b = a-y.transpose()

    res = np.dot(x[:,j],b.transpose())
    gr = res/len(x)
    return gr

def gradient_algorithm(x,y,alpha=1,ep=0.01,max_iter=100000):
    theta = np.ones(len(x[0]))
    temp = np.zeros(len(x[0]))

    jit=[]
    jval=[]

    jj = cost(theta,x,y)
    it = 0

    jit.append(it)
    jval.append(jj)
    converge = False

    while not converge:
        for j in range(len(x[0])):
            temp[j] = theta[j] - (alpha * derivative(theta,x,y,j))
        theta = temp[:]
        temp = np.zeros(len(x[0]))

        jit.append(it)
        jval.append(jj)
        e = cost(theta,x,y)
        if abs(jj-e)<=ep:
            print("converged at iteration: ")
            print(it)
            converge = True
        jj = e
        it = it + 1

        if it>=max_iter:
            print("max iteration exceeded!")
            converge = True
    return theta,jit,jval


if __name__=="__main__":
    x = np.array([[1 , 2104,5,1,45,460],[1,1416,3,2,40,232],[1,1534,3,2,30,315],[1,852,2,1,36,178]])
    y = x[:,5]
    x = x[:,0:5]

    y = y.reshape(len(y),1)
    x = x.astype(float)
    y = y.astype(float)
    for j in range(1,len(x[0])):
        for i in range(len(x)):
            x[i,j]=(x[i,j]-np.average(x[:,j]))/(np.max(x,0)[j]-np.min(x,0)[j])

    th=[]
    jit=[]
    jval=[]
    
    th,jit,jval=gradient_algorithm(x,y)
    
    plt.plot(jit[0:100],jval[0:100])
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.title("Cost VS Iteration")
    plt.show()
    print("Theta :")
    print(th)
