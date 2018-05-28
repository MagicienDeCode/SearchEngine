#! /usr/bin/python3

from readFiletoMatrice import *
from calculatePageRank import *
import sys
import os

def parseArgs(args):
    file = None
    for arg in args:
        splited = arg.split("=")
        if splited[0] == "file":
            file = splited[1]
    return file

file_path = parseArgs(sys.argv[1::])
if file_path == None or not file_path.endswith(".txt") or not os.path.exists(file_path):
	print("wrong args: exemple make pagerank file=data/xxx.txt")
	exit(-1)

matrice = MatriceCLI(file_path)

result = pageRank(0.15, 0.001, matrice.getCLI(), matrice.getInitRank())

print(result)
