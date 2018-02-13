# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 06:06:01 2017

@author: Loukit
"""

from Material.Material import Material
#from Material.ElasticMaterial import ElasticMaterial

import numpy as np
from Element.Element import Element



m2 = Material.newMaterial('elastic','threed')
m2.setElasticProperties(10e6,0.2,1e7)
elastic = np.zeros((6,6))
m2.ElasticityMatrix(elastic)
print(elastic)


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
an = e.shape(1.0,1.0,[1,1,3,4,5,6,7,8])
print(an)
