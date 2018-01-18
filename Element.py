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
        str = np.zeros(self.nstress)
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


#e1=ElementQuad2D()
#e2=Element.newElement("quad8")
e3=Element.newElement("hex20")
e3.setElemConnectivities([1.0,2.0,3.0],2)
e3.setElemConnectivities([1.0,2.0])
e3.setMaterialName("elastic")
print(e3.matName)        