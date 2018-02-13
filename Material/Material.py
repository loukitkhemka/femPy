# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#from Mat.ElasticMaterial import ElasticMaterial
class Material(object):

    def newMaterial(matPhysLaw, stressState):
        if (matPhysLaw=="elastic"):

            return ElasticMaterial(stressState)
    
    def setElasticProperties(self,e,nu,alpha):
        self.e = e
        self.nu = nu
        self.alpha = alpha        
    
    def setPlasticProperties(self, sigY,kM, mM): #sigY - Yield Stress kM-Hardening Coefficient mM-Hardening Power    
        self.sigY=sigY
        self.kM=kM
        self.mM=mM

    def getLambda(self): #Returns Lambda
        if self.StressState=="plstress":
            return self.e*self.nu/((1+self.nu)*(1-self.nu))
        else:
            return self.e*self.nu/((1+self.nu)*(1-2*self.nu))
        
    def getMu(self): #Returns Mu. Mu and Lambda are Lame's Constants
        return 0.5*(self.e)/(1+self.nu)
    
#Material Class Definition Ends Here


        
class ElasticMaterial(Material):
    def __init__(self,StressState):
        
        self.StressState = StressState
        if self.StressState=='threed':
            self.lv=6  #lv is length of stress and strain vectors
        else:
            self.lv=4
    

    def StrainToStress(self,elm,ip):
        deps=elm.getStrainsAtIntPoint(ip)
        temp=elm.getTemperatureAtIntPoint(ip)
        mu=Material.getMu(self) #Mu and lamda are the Lame's Constants
        lamda=Material.getLambda(self)
        beta=lamda+2.0*mu
        at=self.alpha*temp
        dsig=[0]*self.lv
        
        if self.StressState=='threed': #When stress state is three-dimensional,
            deps[0]-=at #the components of strain vector are ex, ey,ez,gamxy, gamyz,gamxz
            deps[1]-=at #Only the normal strain components are to be subtracted by alpha*temp
            deps[2]-=at
            dsig[0]=beta*deps[0]+lamda*(deps[1]+deps[2])#the components of stress vector
            dsig[1]=beta*deps[1]+lamda*(deps[0]+deps[2])#have same coressponding coordinates
            dsig[2]=beta*deps[2]+lamda*(deps[0]+deps[1])#as strain vector
            dsig[3]=mu*deps[3]
            dsig[4]=mu*deps[4]
            dsig[5]=mu*deps[5]
        else:
            deps[0]-=at #When the stress state is 2-dimensional, the components of strain vector are ex, ey,gamxy,ez
            deps[1]-=at
            if self.StressState!='plstress':
               deps[3]-=at
            dsig[0]=beta*deps[0]+lamda*(deps[1]+deps[2])#the components of stress vector
            dsig[1]=beta*deps[1]+lamda*(deps[0]+deps[2])#have same coressponding coordinates as the strain vector
            dsig[2]=mu*deps[2]
            dsig[3]=0.0
            if self.StressState=='plstrain':
                dsig[3]=self.nu*(dsig[0]+dsig[1])-self.e*at
            if self.StressState=='axisym':
                dsig[3]=beta*deps[3]+lamda*(deps[0]+deps[1])
            
        for i in range(0,self.lv-1):
            elm.str[ip].dStress[i]=dsig[i]
    
    def ElasticityMatrix(self,emat):
        if self.StressState=='threed':
            self.ElasticityMatrix3D(emat)
        else:
            self.ElasticityMatrix2D(emat)
            
    def ElasticityMatrix3D(self,emat):
        mu=self.getMu()
        lamda=self.getLambda()
        beta=lamda+2*mu
        #emat=np.zeros((6,6))
        emat[0,0]=emat[1,1]=emat[2,2]=beta
        emat[3,3]=emat[4,4]=emat[5,5]=mu
        emat[0,1]=emat[1,0]=emat[0,2]=emat[2,0]=emat[1,2]=emat[2,1]=lamda
        print(emat)
    
    def ElasticityMatrix2D(self,emat):
        mu=self.getMu()
        lamda=self.getLambda()
        beta=lamda+2*mu
        #emat=np.zeros((4,4))
        emat[0,0]=emat[1,1]=emat[3,3]=beta
        emat[2,2]=mu
        emat[0,1]=emat[1,0]=emat[0,3]=emat[3,0]=emat[1,3]=emat[3,1]=lamda
        
#Elastic Material Class ends here

