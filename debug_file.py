# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 06:06:01 2017

@author: Loukit
"""

from Material import Material,ElasticMaterial
import numpy as np

m1=ElasticMaterial('threed',10e6,0.2,1e7)
elastic = np.zeros((6,6))
m2.ElasticityMatrix(elastic)
print(elastic)

m1=ElasticMaterial('threed',10e6,0.2,1e7)
print(m1.sigY)

m2 = Material.newMaterial('elastic','threed')
m2.setElasticProperties(10e6,0.2,1e7)
