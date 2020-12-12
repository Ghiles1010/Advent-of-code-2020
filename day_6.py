import re


input = open("t.txt").read()

groups = re.split(r"\n\n", input)
groups = list(map(lambda str : str.split("\n"), groups))

sum = 0

for group in groups:
	dic = {}
	num_persons = len(group)
	for person in group:
		for answer in person:
			dic[answer] = dic.get(answer, 0) + 1

	for a in dic:
		if dic[a] == num_persons:
			sum += 1

print(sum)
print(dic)