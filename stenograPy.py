# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 13:49:21 2018
@author: Joel Velez
"""
import encode
import decode
        
class stenograPy():
    def __init__(self):
        self.e = encode.Encode()
        self.d = decode.Decode()
    def main(self):
        a = input("Would you like to encode(E) or decode(d) \n press x to exit \n")
        if a == "e" or a == "E":
            self.e.encodeMain()
        elif a == "d" or a == "D":
            self.d.decodeMain()

if __name__ == '__main__':
    stenograPy.main()
            