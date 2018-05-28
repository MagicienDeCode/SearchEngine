import re
import os

data_path = "data"

def readFile(fileName):
    comment = []
    list = []
    with open(fileName) as f:
        for line in f.readlines():
            if re.search(r'#', line):
                comment.append(line)
            else:
                subList = line.split()
                tuple = (int(subList[0]), int(subList[1]))
                list.append(tuple)

    list.sort(key = lambda tup: (tup[0], tup[1]))

    sortDir = "sortData"
    if not os.path.exists(sortDir):
        os.mkdir(sortDir)
    outfileName = os.path.join(sortDir, fileName.split('/')[1])
    with open(outfileName,"w+") as f:
        for c in comment:
            f.write(c)
        for nSrc,nDes in list:
            f.write(str(nSrc)+"\t"+str(nDes)+"\n")

for path, subdirs, files in os.walk(data_path):
    for name in files:
    	if name.endswith("txt"):
    		readFile(os.path.join(data_path,name))