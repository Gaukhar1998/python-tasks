x=1
size=8
for i in range(size):
	print((' '*(size-i))+bin(x)[4:].replace('0',' ').replace('1',' *'))
	x^=x<<1