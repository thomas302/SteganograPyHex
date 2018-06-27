# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
# Basic tools for working with hex data
#Hex String Tools
import binascii

class stringTools():
    def stringToHex(self, userInput):
        a = binascii.hexlify(userInput)
        return a
    def hexToString(self, userInput):
        a = binascii.unhexlify(userInput)
        return a
    
class fileTools():
    def hexDumpFile(self, userInput):
        chunks = []
        with open(userInput, 'rb') as f:
            for chunk in iter(lambda: f.read(8), b''):
                chunks.append(binascii.hexlify(chunk))
        return chunks
    def readChar(self, userInput):
        charListTemp = []
        charListFinal = []
        with open(userInput, 'rb') as f:
            for chunk in iter(lambda: f.read(4), b''):
                charListTemp.append(binascii.hexlify(chunk))
        for i in range(len(charListTemp)):
            charListFinal.append(charListTemp[i][6:])
        return charListFinal
if __name__=='__main__':
    st = stringTools()
    ft = fileTools()
    print(ft.readChar("data.jpeg"))
