# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:57:05 2017

@author: salman
"""
import pandas as pd
import os

def convert(data_f,rel_name):
    #this function takes 2 argument one is pandas data frame another one is the name of the relation
    print("Creating a .arff file...")
    
    #open the file for write if not exist then create
    file = open("%s.arff" % rel_name,"w+")
    
    #get the all columns name
    col = data_f.columns
    
    print("Processing...\n")
    
    #relation name
    file.write("@relation %s\n"%rel_name)
    
    #go through all the columns to process one by one
    for name in col:
        
        if data_f[name].dtype.kind in 'ifc':
            #checking wheather this column is numeric or not
            file.write("@attribute %s NUMERIC\n"%name)
            
        elif data_f[name].dtype.kind in 'd':
            #checking wheather this column is date or not
            file.write("@attribute %s date\n"%name)
            
        else:
            #it handles nominal attributes
            file.write("@attribute %s {"%name)
            unq = dt[name].unique()
            for i in range(0,unq.size):
                if i!=(unq.size-1):
                    file.write("%s,"%unq[i])
                else:
                    file.write("%s}\n"%unq[i])
                
    file.write("@data\n")
    file.write("%\n")
    print("Putting data...\nIt may take some times...")
    for i in range(0,data_f.shape[0]):
        for j in range(0,data_f.shape[1]):
            if j!=(data_f.shape[1]-1):
                file.write("%s,"%data_f.iloc[i,j])
            else:
                file.write("%s\n"%data_f.iloc[i,j])
                
    file.write("%\n")
    file.close()
    return True
    
#main function goes from here
if __name__ == "__main__":
    
    res=False
    rel_name=input("input the file name to process: ")
    
    #csv file must contain the column names
    if os.path.isfile("%s.txt"%rel_name)==True:
        dt = pd.read_csv("%s.txt"%rel_name)
        res=convert(dt,rel_name)
        print("Your file is ready.")
        
    elif os.path.isfile("%s.csv"%rel_name)==True:
        dt = pd.read_csv("%s.csv"%rel_name)
        res=convert(dt,rel_name)
        print("Processing Done!")
        
    else:
        print("There are no %s file exist in the directory!"%rel_name)
    
    if res==True:
        print("your file is ready.")
    else:
        print("Something is wrong! :( ")
        
    
    