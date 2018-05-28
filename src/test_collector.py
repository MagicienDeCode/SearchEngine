#! /usr/bin/python3

from collector import *

def parseArgs(args):
	path_data = ""
	path_dict = ""
	path_ignore = ""
	path_dict_dir = ""
	list_dicts = []
	for arg in args:
		splited = arg.split("=")
		if splited[0] == "data":
			path_data = splited[1]
		if splited[0] == "dict":
			path_dict = splited[1]
		if splited[0] == "ignore":
			path_ignore = splited[1]
		if splited[0] == "dir":
			path_dict_dir = splited[1]
		if len(splited) == 1:
			list_dicts.append(splited[0])
	if len(path_data) < 1 and len(path_dict) < 1 :
		path_data = list_dicts[0]
		path_ignore = list_dicts[len(list_dicts)-1]
		list_dicts = list_dicts[1:len(list_dicts)-1]
	return (path_data,path_dict_dir,path_dict,path_ignore,list_dicts)

path_data,path_dict_dir,path_dict,path_ignore,list_dicts = parseArgs(sys.argv[1::])

collector = get_collector(path_data,path_dict_dir,path_dict,path_ignore,list_dicts)

print(collector)
