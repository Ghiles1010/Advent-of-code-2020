import re


input = open("t.txt").readlines()

seats = []

for i in range(128):
	for j in range(8):
		seats.append((i,j)) 

def dich(min, max, code, low):

	for letter in code : 
		mid = (min+max)/2
		(min, max) = (min, mid) if letter == low else (mid, max)

	return min if row_c[-1]==low else max-1


max = 0

for code in input :

	row_c = code[:7]
	col_c = code[7:10]

	row = dich(0, 128, row_c, "F")
	col = dich(0, 8, col_c, "L")

	index = seats.index((row,col))
	del seats[index]

	id = row * 8 + col

	if id > max :
		max = id


print(max)
print(seats) # see the one in the middle


