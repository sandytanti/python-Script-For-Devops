#program20.py
#Crate a reusable function which can copy alternat lines of code , one file to another file

def copy_file(s,d):
	file1 = open(s,'r')
	data = file1.readlines()
	file2 = open(d,'a')
	i = 0
	while i < len(data):
		file2.write(data[i])
		i = i + 2

#main program
copy_file("E:/sample.txt","E:/sample5.txt")
copy_file("E:/kubernetes.txt","E:/kubernetes2.txt")




