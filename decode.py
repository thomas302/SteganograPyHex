# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
import hexTools

class Decode():
    def __init__(self):
        self.decoded = []
        self.ft = hexTools.fileTools()
        self.st = hexTools.stringTools()
        
    def decode(self):
