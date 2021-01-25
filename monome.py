# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:52:48 2021

@author: hdafa
"""

class Monome:
    def __init__(self, coef, deg, suivant=None):
        # donnée :
        self.coef = coef # de type float
        self.deg = deg # de type int
        # une reference vers le prochain monome (par défault None)
        self.suivant = suivant # de type Monome
        
    def getCoef(self):
        return self.coef
    def setCoef(self, val):
        self.coef = val
        return self
    
    def getDeg(self):
        return self.deg
    def setDeg(self, val):
        self.deg = val
        return self
    
    def getSuivant(self):
        return self.suivant
    def setSuivant(self, m):
        self.suivant = m
        return self
    
    def __str__(self):
        return str(self.getCoef()) + 'X^' + str(self.getDeg())
    
    def __mul__(self, m):
        return Monome(self.getCoef() * m.getCoef(), self.getDeg()+m.getDeg())
    
    def __add__(self, m):
        assert self.getDeg() == m.getDeg()
        return Monome(self.getCoef() + m.getCoef(), self.getDeg())
    
    def __sub__(self, m):
        pass
    
    def __truediv__(self, m):
        pass
    
    @staticmethod
    def deriver(m):
        pass
    
    @staticmethod
    def primitive(m):
        pass
    
    
    
        
        
        
        
        
    