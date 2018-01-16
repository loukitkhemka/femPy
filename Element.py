# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:24:44 2018

@author: lokith
"""
from abc import ABC, abstractmethod
#from enum import Enum
import numpy as np

class Element(ABC):
    #class elements(Enum):
        #quad8 = 1
        #hex20 = 1

    def newElement(name):
        if (name == "quad8"):
            return ElementQuad2D()
        elif (name == "hex20"):
            return ElementQuad3D()
        else:
            print("Incorrect Element Type: "+ name)
    
    
    @abstractmethod
    def __init__(self, name, nind, nstress):
        self.name = name
        self.nind = nind
        self.nstress = nstress
        ind = np.zeros(self.nind,dtype=np.int)
        str = np.zeros(self.nstress)
        print(ind)
        print(str)
        print("Printing Done!")

class ElementQuad2D(Element):
    def __init__(self):
        print("Instantiating ElementQuad2D class")
        super().__init__("quad8",8,4)

class ElementQuad3D(Element):
    def __init__(self):
        super().__init__("hex20",20,8)


#e1=ElementQuad2D()
#e2=Element.newElement("quad8")
e3=Element.newElement("hex20")
        