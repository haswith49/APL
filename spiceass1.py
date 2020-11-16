import sys
arg1 = sys.argv[1]
netlist=arg1.find('.netlist')
try:
	if netlist==-1:#for checking whether file is .netlist 
		print("error opening the file")
	else:
		f=open(arg1)
		o=f.readlines()
		f.close()
		l=len(o)
	
	for m in range(l):
		a=o[m].split('\n')#to remove ending character \n
		o[m]=a[0]
	start=o.index('.circuit')#find line no. containing .circuit
	#if start not :
	#	print("this file does not contain .circuit")
	end=o.index('.end')
	o.reverse()
	for i in range(start+1,end):
		#o[i]=o[i].strip()# to remove leading and trailing characters
		b=o[i].split('#')# to remove comments
		o[i]=b[0].split()
		for j in range(len(o[i])-1,-1,-1):
			print(o[i][j],end=' ')
		print()
except Exception as ex:
	print("Input file is corrupted")

		
