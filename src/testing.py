#! /usr/bin/python3

from readFiletoMatrice import *
from calculatePageRank import *

import os

data_path = "sortData"
src_data_path = "data"

def testPageRank(path_filetxt,path_fileres):
	print("*"*30 + path_filetxt + "*"*30)
	matrice = MatriceCLI(path_filetxt)
	print("="*10 + " expected "+"="*10)
	for row in open(path_fileres).readlines():
		print(row.strip("\n"))
	print("="*10 + " my result "+"="*10)
	print(pageRank(0.15, 0.001, matrice.getCLI(),matrice.getInitRank()))
	print()


for path, subdirs, files in os.walk(data_path):
	for name in files:
		if name.endswith("txt"):
			testPageRank(os.path.join(data_path,name),os.path.join(src_data_path,name[0:len(name)-3])+"res")