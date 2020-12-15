import re

input = open("t.txt").readlines()
input = list((map(lambda str: eval(str),input)))

low, top, num = 0, 25, 25 

while num < len(input):
	error = True
	for i in range(low, top):
		for j in range(low, top):
			if input[i] != input[j] and input[i]+input[j] == input[num]:
				error = False

	if error:
		err = input[num]
		break

	low += 1
	top += 1
	num += 1

print(err)

contig = None

for low in range(num+1):
	for i in range(low+1, num+1):
		if sum(input[low:i+1]) == err:
			contig = input[low:i+1]
			break
	if contig != None:
		break

code = min(contig) + max(contig)
print(code)

