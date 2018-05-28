# FAN-LI 2018 Projet-maain M2
Python3 PageRank

# Getting Started
To run the test of PageRank, cd into the root folder and run:
```bash
make testpagerank
```
To get PageRank of one sorted file, open the Terminal: indicate the path of file
```bash
make pagerank file=[path_of_file]
```
for exemple:
```bash
make pagerank file=sortData/xxx.txt
```

To get collector, open the Terminal:
```bash
python3 src/test_collector.py [path_data] [dict1] [dict2] [...] [path_ignore]
or
make collector data=[path] dict=[path] ignore=[path]
or
make collector data=[path] dir=[path] ignore=[path]
```
for exemple:
```bash
python3 src/test_collector.py metaData/amazon-meta.txt wordsArchive/englishWords.txt wordsIgnore/prepositions.txt
or
make collector data=metaData/amazon-meta.txt dict=wordsArchive/englishWords.txt ignore=wordsIgnore/prepositions.txt
or
make collector data=metaData/amazon-meta.txt dir=wordsArchive ignore=wordsIgnore/prepositions.txt
```

To search:
modify config.json for your own data:
1.pagerank_file
2.amazon_data
3.dict_dir: the folder of dictionnary
4.dict_ignore: the path of dictionnary
!! by default, we use the data of tests.
```bash
make search words=[word1,word2,word3,...]
```
for exemple:
```bash
make search words=wake,up,worlds
```
format of result:
(id,pagerank)
********Searching results********
(15, 1.016473164352883)
(13, 0.03996231621034525)
