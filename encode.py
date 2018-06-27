# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
class Encode():
    def replaceBytes(byteList, hexStringList):
        for i in range(len(hexStringList)):
            byteList[i] = byteList[i] + hexStringList[i]
        return byteList

    def encode():
        
