#! /usr/bin/python3
import json, sys, os
from readFiletoMatrice import *
from calculatePageRank import *
from collector import *


def load_config():
    # OPEN CONSTANTS IN config.json
    with open("config.json") as config_data:
        config = json.load(config_data)
        settings = config["settings"]

        pagerank_file = settings["pagerank_file"]
        amazon_data = settings["amazon_data"]
        dict_dir = settings["dict_dir"]
        dict_ignore = settings["dict_ignore"]

    ignore_list = parserIgnore(dict_ignore)
    matrice = MatriceCLI(pagerank_file)
    print("*"*10 + "load pageRank" + "*"*10)
    result = pageRank(0.15, 0.001, matrice.getCLI(), matrice.getInitRank())
    print(result)
    print("total count : "+ str(len(result)))
    print("*"*10 + "load collector" + "*"*10)
    collector = get_collector(amazon_data,dict_dir,"",dict_ignore,"")
    print(collector)
    return ignore_list,result,collector


def search():
    args = sys.argv[1]
    list_words = args.split("=")[1]
    list_words = list_words.split(",")

    # eliminate double
    list_words = list(set(list_words))

    ignore_list,pagerank,collector = load_config()
    # excludes words
    for index, w in enumerate(list_words):
        if w in ignore_list:
            del list_words[index]

    list_ids = findIdsByWords(collector,list_words)

    if(len(list_ids) == 0):
        print("*" * 10 + "Searching results" + "*" * 10)
        print("Result not found")
        return 0

    result = {}
    for id in list_ids:
        id = int(id)
        if id in result:
            result[id] = 1 + result[id]
        else:
            result[id] = pagerank[id]
    result = sorted(result.items(),key = lambda d:d[1],reverse = True)

    print("*"*10+"Searching results"+"*"*10)
    for r in result:
        print(r)

    return 0


search()
