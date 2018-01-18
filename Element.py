# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:24:44 2018

@author: lokith
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
        str = StressContainer(self.nstress)
        print(ind)
        print(str)
        print("Printing Done!")
    
    #Set Element Connectivities
    #indel - Connectivity Numbers
    #nind - Number of element Nodes
    def setElemConnectivities(self,indel, nind=None):
        self.ind = np.copy(indel[0:len(indel) if nind is None else nind])
        print(self.ind)
    
    def setMaterialName(self,name):
        self.matName = name
        print(self.matName)
    
    #Do setlemXy and setElemXyT after fininshing fem class

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
    # ind - connectivity numbers
    
    
    def degeneration(self,ind):
        deg = 0
        for i in range(0,7,2):
            print(i)
            if ind[i] is ind[i+1]:
                deg = (i+5) % 8
                break
        return deg








#e1=ElementQuad2D()
#e2=Element.newElement("quad8")
e3=Element.newElement("hex20")
e3.setElemConnectivities([1.0,2.0,3.0],2)
e3.setElemConnectivities([1.0,2.0])
e3.setMaterialName("elastic")
print(e3.matName)       
i = range(7,2)
for j in i:
    print(j)
e = ShapeQuad2D()
e.degeneration([1.0,2.0,3.0,3.0,5.0,6.0,7.0,7.0])