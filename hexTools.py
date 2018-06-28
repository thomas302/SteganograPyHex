# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
#Basic tools for working with hex data
#Hex String Tools
import binascii

class stringTools():
    def stringToHex(self, userInput):
        a = binascii.hexlify(userInput)
        return a
    
    def hexToString(self, userInput):
        a = binascii.unhexlify(b''.join(userInput))
        return a
    
    def splitByN(self, seq, n):
        """A generator to divide a sequence or string into chunks of n units."""
        s = seq
        o = []
        while s:
            o.append(s[:n])
            s = s[n:]
        return o

    
class fileTools():
    def hexDumpFile(self, userInput):
        chunks = []
        with open(userInput, 'rb') as f:
            for chunk in iter(lambda: f.read(8), b''):
                chunks.append(binascii.hexlify(chunk))
        return chunks
    def writeToFile(self, byteList, fileOut):
        with open(fileOut, 'wb') as fout:
            byteList = b''.join(byteList)
            fout.write(binascii.unhexlify(byteList))
    def readChar(self, userInput):
        charListTemp = []
        charListFinal = []
        with open(userInput, 'rb') as f:
            for chunk in iter(lambda: f.read(8), b''):
                charListTemp.append(binascii.hexlify(chunk))
        for i in range(len(charListTemp)):
            charListFinal.append(charListTemp[i][14:])
        return charListFinal
    
if __name__=='__main__':
    st = stringTools()
    ft = fileTools()
    