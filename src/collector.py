#! /usr/bin/python3

from trie import *
import re
from string import punctuation
import sys
import os

#return a list of ignore words
def parserIgnore(path_of_ignore):
	ignore_list = []
	with open(path_of_ignore) as f_ignore:
		line = f_ignore.readline().strip("\n").lower()
		while line:
			ignore_list.append(line)
			line = f_ignore.readline().strip("\n").lower()
	return ignore_list

def parserDictionary(path_of_dictionary,my_trie,ignore_list):
	with open(path_of_dictionary) as f_dictionary:
		line = f_dictionary.readline().strip("\n").lower()
		while line:
			if line not in ignore_list:
				my_trie.insert(line)
			line = f_dictionary.readline().strip("\n").lower()

#return a structure of my_trie
def parserOneDict(path_of_dictionary,path_of_ignore):
	my_trie = Trie()
	ignore_list = parserIgnore(path_of_ignore)
	parserDictionary(path_of_dictionary,my_trie,ignore_list)
	return my_trie

#return a structure of my_trie
def parserDictionaryList(list_files,path_of_ignore):
	my_trie = Trie()
	ignore_list = parserIgnore(path_of_ignore)
	for f in list_files:
		parserDictionary(f,my_trie,ignore_list)
	return my_trie



#return a dict of collector { word -> [1,2,23] }
def parserAmazonData(my_dict,path_of_amazon_data):
	collector = {}
	count = 0
	now_id = 0
	with open(path_of_amazon_data) as f:
		line = f.readline()
		while line:
			if re.search(r'Id:',line):
				count += 1
				line = re.sub("[" + punctuation + "]", "", line)
				line = line.strip("\n").lower();
				now_id = line.split()[1]
			if re.search(r'title:',line):
				line = line.replace("title:","",1)
				line = line.strip("\n").lower();
				line = re.sub("[" + punctuation + "]", "", line)
				for word in line.split():
					if my_dict.search(word):
						if word not in collector:
							collector[word] = []
							collector[word].append(now_id)
						else:
							collector[word].append(now_id)
			if count > 19:
				break
			line = f.readline()
	print("total count :" + str(count))
	return collector

#return a list of ids that contains the words
def findIdsByWords(collector,list_words):
	list_ids = []
	for word in list_words:
		if word in collector:
			for each_id in collector[word]:
				list_ids.append(each_id)
	#list_ids = list(set(list_ids))
	return list_ids

#Interface return a dict of collector { word -> [1,2,23] }
def get_collector(path_of_amazon_data,path_of_dict_dir,path_of_dictionary,path_of_ignore,list_dicts):
	if len(path_of_dictionary) > 1 :
		my_trie = parserOneDict(path_of_dictionary,path_of_ignore)
	if len(path_of_dict_dir) > 1 :
		list_files = []
		for path, subdirs, files in os.walk(path_of_dict_dir):
			for name in files:
				if name.endswith("txt"):
					list_files.append(os.path.join(path_of_dict_dir,name))
		my_trie = parserDictionaryList(list_files,path_of_ignore)
	if len(list_dicts) > 0 :
		my_trie = parserDictionaryList(list_dicts,path_of_ignore)
	return parserAmazonData(my_trie,path_of_amazon_data)
