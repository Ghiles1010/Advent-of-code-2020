import re


input = open("t.txt").read()
passports = input.split("\n\n")

colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
keys = ["eyr", "iyr", "byr", "ecl", "pid", "hcl", "hgt"]

def is_between(str, n1, n2) :
	return True if n1 <= eval(str) <= n2 else False

eyr = lambda str : is_between(str, 2020, 2030)
iyr = lambda str : is_between(str, 2010, 2020)
byr = lambda str : is_between(str, 1920, 2002)
ecl = lambda str : True if str in colors else False
pid = lambda str : True if re.match(r"\d{9}$", str) else False
hcl = lambda str : True if re.match(r"#[0-9a-f]{6}$", str) else False
cid = lambda str : True

def hgt(str):
	if res := re.search(r"(\d{2,3})(cm|in)", str):		
		taille = res.group(1)
		unit = res.group(2)
		return is_between(taille, 150, 193) if unit == "cm" else is_between(taille, 59, 76)




print(passports[0])

err = 0

for p in passports:

	keys_ok =True

	for k in keys:
		if not k in p:
			err += 1
			keys_ok = False
			break

	if keys_ok :

		infos = re.split("\n| ", p)

		for i in infos :
			key, val = i.split(":")
			if not globals()[key](val):
				err+=1
				break


v = len(passports) - err
print(v)

