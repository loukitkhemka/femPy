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
        