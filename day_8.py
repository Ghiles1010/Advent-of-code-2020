import re

input = open("t.txt").readlines()



# prepare data
def init(input):
	lis = []
	for i in input :
		inst, val = i.split()
		lis.append([(inst, eval(val)), False])
	return lis




def flip(lis, i):
	inst, val = lis[i][0]
	lis[i][0] = ("nop",val) if lis[i][0][0] == "jmp" else ("jmp",val) 
	return lis


def execute(lis):
	num_inst, acc, i, ended = len(lis), 0, 0, True

	while i < num_inst:

		if lis[i][1] == True :
			ended = False
			break

		#print("here",i, lis[i][0])
		inst, val = lis[i][0]


		if inst == "jmp":
			i += val-1 #-1 beacause of the plus 1 de plus tard

		elif inst ==  "acc":
			acc+=val

		lis[i][1] = True
		i += 1
	return (acc, ended)

lis = init(input)


for i in range(len(lis)):

	inst, val = lis[i][0]

	if inst=="nop" and val == 0:
		continue

	if inst=="jmp" or inst=="nop":
		
		lis = init(input)
		lis = flip(lis, i)
		acc, ended = execute(lis)

		if ended:
			break

		lis = flip(lis,i)



print(acc)


