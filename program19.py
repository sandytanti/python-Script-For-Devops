#program19.py
#Crate a reusable function which can copy alternat lines of code , one file to another file

source = input("Enter the source filename :")
dest = input("Enter the destination filename :")

def copy_file(s,d):
	file1 = open(s,'r')
	data = file1.readlines()
	file2 = open(d,'a')
	i = 0
	while i < len(data):
		file2.write(data[i])
		i = i + 2

#main program
copy_file(source,dest)


