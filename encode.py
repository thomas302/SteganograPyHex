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
        for i in range(len(hexStringList)):
            byteList[i] = byteList[i] + hexStringList[i]
        return byteList
    def encodeData(self, f, s):
        l1 = f[:100]
        l2 = f[100:]
        l3 = []
        l4 = f[100-len(s):]
        for i in range(len(s)):
            l3.append(l2[i].replace(l2[i], l2[i][:14]+s[i]))
        f = l1+l3+l4
        return f
    def encodeMain(self, string, inputFile, outPutFile):
        s = self.st.stringToHex(string)
        s = self.st.splitByN(s, 2)
        file = self.ft.hexDumpFile(inputFile)
        fileOut = self.encodeData(file, s)
        self.ft.writeToFile(fileOut, outPutFile)

        
if __name__  ==  "__main__":
    e = Encode()
    e.encodeMain(b"this is text", "data.png", "stuff.png")