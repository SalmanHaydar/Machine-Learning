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
    p = np.sum((np.dot(theta,x[i].reshape(len(x[0]),1)) - y[i])**2 for i in range(len(x)))
    j = p/(2*len(x))
    return j

def derivative(theta,x,y,j):
    gr = np.sum((np.dot(theta,x[i].reshape(len(x[0]),1)) - y[i]) * x[i][j] for i in range(len(x)))/len(x)
    return gr

def gradient_algorithm(x,y,alpha=0.01,ep=0.01,max_iter=10000):
    theta = np.ones(len(x[0]))
    temp = np.zeros(len(x[0]))
    jj = cost(theta,x,y)
    it = 1
    converge = False

    while not converge:
        for j in range(len(x[0])):
            temp[j] = theta[j] - (alpha * derivative(theta,x,y,j))
        theta = temp[:]
        temp = np.zeros(len(x[0]))
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
    return theta


if __name__=="__main__":
    x = np.array([[1 , 2104,5,1,45,460],[1,1416,3,2,40,232],[1,1534,3,2,30,315],[1,852,2,1,36,178]])
    y = x[:,5]
    x = x[:,0:5]
    x = x.astype(float)
    y = y.reshape(len(y),1)
    for j in range(1,len(x[0])):
        for i in range(len(x)):
            x[i,j]=(x[i,j]-np.average(x[:,j]))/(np.max(x,0)[j]-np.min(x,0)[j])
    y = y.astype(float)
    for i in range(len(y)):
        y[i,0]=(y[i,0]-np.average(y[:,0]))/(np.max(y,0)[0]-np.min(y,0)[0])

    print(x)
    print(y)
    th=[]
    th=gradient_algorithm(x,y)
    print(th)
