#program15.py
#Program to copy contain from one file into another file 

file1 = open("E:/kubernetes.txt",'r')
data = file1.read()
file2 = open("E:/k2.txt",'w')
file2.write(data)


