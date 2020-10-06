def pair(p):
	for i in p:
		c = bin(i).strip('0b')
		if (c.count("1") % 2 == 0):
			d = '0' + c
			e = bytearray(d, 'utf-8')
		else:
			d = '1' + c
			e = bytearray(d, 'utf-8')
	print(e)

a = bytearray(input("entrez un mot: "), 'utf-8')

pair(a)
