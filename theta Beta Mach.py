# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 14:45:57 2023

@author: Dell
"""

"""
This is a block code for computing OSW properties
"""

# The code takes inflow Mach number and gas properties


import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from sympy import*

# Flow
M_1 = 1;


gamma = 1.4     #gas constant
gamman = (gamma-1)
gammap = (gamma+1)
rad = np.pi/180   #conversion from degree to radian
deg = 1/rad
tmax = np.zeros(10)
for j in range(1,10):
 beta_min = np.arcsin(1/j)         #mach angle
 betai = np.arange(beta_min,np.pi/2,np.pi/200000) 
 theta = np.zeros(betai.size)         #wedge angle
 weak = zeros(10)

 i=0
 betas  = np.zeros((betai.shape))  #this is saying us the shape or no. of elements of the betas is same as the betai
 error = np.zeros((betai.shape))  #same as above
 for k in range(1,betai.size):  #the loop starts at 1 and end at betai.size .size counts the number of element in array
    beta = betai[k]
    a1 = ((j*np.sin(beta))**2)-1;
    a2 = ((j**2)*(gamma+np.cos(2*beta)))+2  
    a3 = 2*1/(np.tan(beta))
    theta[k]= np.arctan((a3*(a1/a2)))
    ang = np.arctan((a3*(a1/a2)))
    tmax[i] = deg* np.max(theta)
    max_position = pd.Series(theeta).idxmax()
    beta1 = 180/np.pi * beeta[0:int(max_position)]
    batm[i] =  180/np.pi * beeta[beta1.size]
    theeta = np.arctan((2 * ((M[i] * np.sin(beeta))**2 - 1) / (np.tan(beeta)*(M[i]**2 * (gamma+np.cos(2*beeta)) + 2)))) # using raltion of thata,beta and M
    tmax[i] = 180/np.pi * np.max(theeta)
    max_position = pd.Series(theeta).idxmax() 
    weak_soln = 180/np.pi * theeta [0:int(max_position)]
    strong_soln = 180/np.pi * theeta[int(max_position)+1:theeta.size]
   #for weak solution 
   
   
    error[k] = np.tan(beta)/np.tan(beta-theta[k]) - gammap*(j*np.sin(beta))**2 / (2+gamman*(j*np.sin(beta))**2)
    error = abs(error)
    if error[k] < 0.0002:
       weak[j] = beta*deg
       
       
       

 plt.plot(theta*deg, batm*deg, label = j)
 plt.plot(tmax,betai*deg)
 # naming the x axis
plt.xlabel('theta')
# naming the y axis
plt.ylabel('beta')
plt.xlim([0,46])
plt.ylim([0, 90])

# giving a title to my graph
plt.title('theta-beta-mach curve')
plt.legend()
  
 