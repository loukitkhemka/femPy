# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:15:49 2018

@author: lokith
"""
import numpy as np
import math

class GaussRule(object):
    def __init__(self,nGauss,nDim):
        self.nGauss = nGauss #Number of Gauss Points in each direction
        self.nDim = nDim #Number of Dimensions
        
        #point locations and weights for 1,2,3-point rules for 2D problems
        __X = [[0.0],[-1.0/math.sqrt(3.0), 1.0/math.sqrt(3.0)],
             [-math.sqrt(0.6), 0.0, math.sqrt(0.6)]]
        __W= [[2.0], [1.0,1.0],[5.0/9.0, 8.0/9.0, 5.0/9.0]]
        
        #point locations and weights for 14-point rule for 3D problem
        __a = 0.7587869106393281
        __b = 0.7958224257542215
        __X14 = [-__a,__a,-__a,-__a,__a,-__a,__a,__a,-__b,__b, 0, 0, 0, 0]
        __Y14 = [-__a,-__a,__a,-__a,__a,__a,-__a,__a, 0, 0,-__b,__b, 0, 0]
        __Z14 = [-__a,-__a,-__a,__a,-__a,__a,__a,__a, 0, 0, 0, 0,-__b,__b]
        __Wa = 0.3351800554016621
        __Wb = 0.8864265927977839
        
        if (not((self.nGauss>=1 and self.nGauss <=3) or (self.nGauss==14))):
            print("Gauss Rule: nGauss has a forbidden value:"+str(self.nGauss))
        elif not(self.nDim>=1 and self.nDim<=3):
            print("Gauss Rule: nDim has forbidden value:"+str(self.nDim))
        else:
            if (self.nGauss==14):
                self.nIntPoints=14
            else:
                #print("HEre")
                self.nIntPoints = 1
                for i in range(self.nDim):
                    self.nIntPoints *= self.nGauss
            
            #xii, eti and zei are the absciscca of the Gauss Rule
            #Integration weights of the Gauss Rule

            self.xii = np.zeros(self.nIntPoints)
            self.wi = np.zeros(self.nIntPoints)
            if self.nDim > 1: 
                self.eti = np.zeros(self.nIntPoints)
            if self.nDim > 2:
                self.zei = np.zeros(self.nIntPoints)
            
            if self.nGauss == 14:
                for i in range(self.nGauss):
                    self.xii[i] = __X14[i]
                    self.eti[i] = __Y14[i]
                    self.zei[i] = __Z14[i]
                    self.wi[i] = __Wa if i<8 else __Wb
            else:
                ip = 0
                n = self.nGauss-1
                if (self.nDim == 1):
                    for i in range(self.nGauss):
                        self.xii[ip] = __X[n][i]
                        #print(__W[n][i])
                        self.wi[ip] = __W[n][i]
                        ip = ip+1
                elif (self.nDim == 2):
                    for i in range(self.nGauss):
                        for j in range(self.nGauss):
                            self.xii[ip] = __X[n][i]
                            self.eti[ip] = __X[n][j]
                            self.wi[ip] = __W[n][i]*__W[n][j]
                            ip=ip+1
                elif(self.nDim == 3):
                    for i in range(self.nGauss):
                        for j in range(self.nGauss):
                            for k in range(self.nGauss):
                                self.xii[ip] = __X[n][i]
                                self.eti[ip] = __X[n][j]
                                self.zei[ip] = __X[n][k]
                                self.wi[ip] = __W[n][i]*__W[n][j]*__W[n][k]
                                ip=ip+1

#Debugging
g = GaussRule(2,1)


def poly_1(x): #1D function for calculation of integration
    i = (x**3)-(2*(x**2))+(3*x)-1
    return i
I=0
for i in range(g.nIntPoints):
    I += poly_1(g.xii[i])*g.wi[i]
print(I)
            
            