import re

input = open("t.txt").readlines()

def contained_in(bag, dic):

	containers = dic.get(bag)

	if containers :
		out = []
		out += containers
		for c in containers:
			out += contained_in(c, dic)
		return out
	else : 
		return []

def contains(bag, dic):
	contained = dic.get(bag)
	sum = 0
	if contained :
		for c in contained:
			rep = eval(c[0])
			sum += rep + rep * contains(c[1], dic)
		return sum
	else : 
		return 0


dic_asc = {}
dic_desc = {}

for line in input:

	info = line.split("contain")
	container = re.search(r"(.+?) bags?", info[0]).group(1)
	contained = re.findall(r"(\d+) (.+?) bags?", info[1][:-2])

	for c in contained:

		dic_desc[container] = dic_desc.get(container, [])
		dic_desc[container].append(c)

		bag = c[1]
		dic_asc[bag] = dic_asc.get(bag, [])
		dic_asc[bag].append(container)

res = set(contained_in("shiny gold", dic_asc)) #enlever les repetitions
reso = contains("shiny gold", dic_desc) 

print(len(res))
print(reso)