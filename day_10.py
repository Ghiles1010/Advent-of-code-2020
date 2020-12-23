
input = open("t.txt").readlines()
input = sorted([int(x) for x in input])
input.append(input[-1]+3) #built-in adapter








differences = {}
volt_p = 0

for volt in input:
	dif = volt-volt_p
	differences[dif] = differences.get(dif, 0) + 1
	volt_p = volt

answer = differences[1]*differences[3]

print(answer)



input = [0] + input #outler

def Next_ad(index):

	indexes = []

	i = 1

	while i <= 3 and (index+i) < len(input) and (input[index+i] - input[index]) <= 3:
		indexes.append(index+i)
		i+=1

	return indexes


dic = {}

def Parcours(i=0):

	next = Next_ad(i)

	if i in dic:
		return dic[i]

	if next == []:
		return 1

	ans = 0

	for j in next:
		ans += Parcours(j)

	dic[i] = ans 
	return ans




print(Parcours())
