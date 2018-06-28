# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
import hexTools
import binascii
class Decode():
    def __init__(self):
        self.decoded = ''
        self.ft = hexTools.fileTools()
        self.st = hexTools.stringTools()
        
    def decodeMain(self, inputFile):
        l = self.ft.readChar(inputFile)
        l = b''.join(l[100:])
        print(binascii.unhexlify(l))
if __name__ == "__main__":
    d = Decode()
    d.decodeMain("stuff.png")