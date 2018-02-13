# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:16:15 2018

@author: Loukit
"""

from abc import ABC, abstractmethod
#from enum import Enum
import numpy as np

class Element(ABC):
    
    
    def newElement(name):
        elements = {'quad8': ElementQuad2D,
                    'hex20': ElementQuad3D}
        try:
            return elements[name]()
        except:
            print("Incorrect Element Type:"+ name)
                
    
    @abstractmethod
    def __init__(self, name, nind, nstress): # Not yet complete
        self.name = name
        self.nind = nind
        self.nstress = nstress
        ind = np.zeros(self.nind,dtype=np.int)
        str = np.zeros(self.nstress)
        print(ind)
        print(str)
        print("Printing Done!")
    
        def setElementConnectivities(self,indel,nind=None):
            nind = len(indel) if nind is None else nind
            ind = np.copy(indel[0:nind])
            print(ind)
        
        
#2D Quadrilateral Element
class ElementQuad2D(Element):
    def __init__(self):
        print("Instantiating ElementQuad2D class")
        super().__init__("quad8",8,4)

#3D Quadrilateral Element
class ElementQuad3D(Element):
    def __init__(self):
        super().__init__("hex20",20,8)

class StressContainer(object):
    def __init__(self,nDim):
        self.sStress = np.zeros(2*self.nDim) #Vector of Accumulated Stress
        self.dStress = np.zeros(2*self.nDim) #Vector of stress increment


class ShapeQuad2D(object):
    
    # Degeneration Check.If the element is triangular, then
    # the method returns a local number (starting from 0) of the 
    # mid-side node opposite to degenerated side
    # For further understanding refer to fig 10.5(b) on page 105 of Nikishkov's Textbook
    # ind - connectivity numbers
    def degeneration(self,ind):
        print("Degeneracy Check")
        self.deg = 0
        for i in range(0,7,2):
            #print(i)
            if ind[i] is ind[i+1]:
                self.deg = (i+5) % 8
                break
        print(self.deg)
        return self.deg
    """
    While corner nodes are always present in the element, Intermediate midside
    nodes can be absent in any order. Absence of a midside node is coded by a 
    zero connectivity number in ind array.
    """
    #Shape functions
    #xi,et - local coordinates
    #ind[8] - element connectivities
    #an[8] - shape functions (output)
    def shape(self, xi, et, ind):
        self.an = np.zeros(8)
        if (ind[1] > 0):
            self.an[1] = 0.5*(1-xi*xi)*(1-et)
        if (ind[3] > 0):
            self.an[3] = 0.5*(1-et*et)*(1+xi)
        if (ind[5] > 0):
            self.an[5] = 0.5*(1-xi*xi)*(1+et)
        if (ind[7] > 0):
            self.an[7] = 0.5*(1-et*et)*(1-xi)
        
        self.an[0] = 0.25*(1-xi)*(1-et)-0.5*(self.an[7]+self.an[1])
        self.an[2] = 0.25*(1+xi)*(1-et)-0.5*(self.an[1]+self.an[3])
        self.an[4] = 0.25*(1+xi)*(1+et)-0.5*(self.an[3]+self.an[5])
        self.an[6] = 0.25*(1-xi)*(1+et)-0.5*(self.an[5]+self.an[7])
        
        self.degeneration(ind) #Checking for Degeneracy by calling Degeneracy Method here
        
        if (self.deg > 0 and ind[1]>0 and ind[3]>0 and ind[5] > 0 and ind[7]>0):
            delta = 0.125*(1-xi*xi)*(1-et*et)
            self.an[self.deg-1] += delta
            self.an[self.deg] -= 2.0*delta
            self.an[(self.deg+1)%8] +=delta
        return self.an






#e1=ElementQuad2D()
#e2=Element.newElement("quad8")
#e3=Element.newElement("hex20")
#e3.setElemConnectivities([1.0,2.0,3.0],2)
#e3.setElemConnectivities([1.0,2.0])
#e3.setMaterialName("elastic")
#print(e3.matName)       
#i = range(7,2)
#for j in i:
#    print(j)
#e = ShapeQuad2D()
#e.degeneration([1.0,2.0,3.0,3.0,5.0,6.0,7.0,7.0])
#an = e.shape(1.0,1.0,[1,1,3,4,5,6,7,8])
#print(an)
