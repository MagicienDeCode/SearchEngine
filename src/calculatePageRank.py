#! /usr/bin/python3

def iterator_CLI(cli,table_v):
	length = len(table_v)
	table_c = cli[0]
	table_l = cli[1]
	table_i = cli[2]
	result = [0 for i in range(0,length)]
	for i in range(0,len(table_l)-1):
		if(table_l[i+1] != table_l[i]):
			for j in range(table_l[i],table_l[i+1]):
				result[table_i[j]] += table_c[j] * table_v[i]
	return result

def pageRank(d,e,cli,table_v):
	def converge(table_1,table_2):
		flag = True
		for i in range(0,len(table_1)):
			if((abs(table_1[i]-table_2[i])) > e ):
				flag = False
		return flag
	times = 0
	while True:
		new_table_v = iterator_CLI(cli,table_v)
		for i in range(0,len(new_table_v)):
			new_table_v[i] = new_table_v[i]*(1-d) + d/(len(cli[1])-1)
		if converge(new_table_v,table_v):
			print("times : "+ str(times))
			return new_table_v
		else:
			times += 1
			table_v = new_table_v