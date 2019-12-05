#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:14:15 2019

@author: abhijithneilabraham
"""

from antlr4 import *
from Python3Parser import Python3Parser
from Python3Lexer import Python3Lexer
from Python3Listener import Python3Listener
import sys

def main(argv):
    ip=FileStream(argv)
    lexer=Python3Lexer(ip)
    stream=CommonTokenStream(lexer)
    parser=Python3Parser(stream)
    tree=parser.NEWLINE()
    op=open('dataset.csv','w')
    Python3Listen=Python3Listener(op)
    walker=ParseTreeWalker()
    walker.walk(Python3Listen,tree)
    parser.parse(argv)
    op.close()
if __name__ == '__main__':
    main(sys.argv)

    
