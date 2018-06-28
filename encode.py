# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
import hexTools
class Encode():
    def __init__(self):
        self.ft = hexTools.fileTools()
        self.st = hexTools.stringTools()
        
    def replaceBytes(self, byteList, hexStringList):
        for i in range(len(3, hexStringList)):
            byteList[i] = byteList[i] + hexStringList[i]
        return byteList
    def writeToFile(self, byteList, fileOut):
        with open(fileOut, 'wb') as fout:
                fout.write(b''.join(byteList))
    def encodeMain(self, string, inputFile, outPutFile):
        s = self.st.stringToHex(string)
        s = self.st.splitByN(s, 2)
        