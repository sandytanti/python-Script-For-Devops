#program10.py
# Display max number in the list 

numbers = [10,20,30,40,50,80]
max = 0

for i in numbers:
	if max < i:
		max = i

print("Maximum numbers in list is :",max)



