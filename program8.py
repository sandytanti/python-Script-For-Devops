#program8.py
# Display the count of odd and even number 

numbers = [1,2,3,4,5,6,7,8,9,10,11]
even = 0
odd = 0
for i in numbers:
	if i % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1
print("count of even numbers is :",even)
print("count of odd numbers is :",odd)



