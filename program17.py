#program17.py
#Copy the alternat data in another file 

file1 = open("E:/sample.txt",'r')
data = file1.readlines()
file2 = open("E:/sample2.txt",'a')
i = 0
while i < len(data):
	file2.write(data[i])
	i = i + 2


