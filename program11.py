#program11.py
# Program to accept the string and count 
#how many digits, letters, special character are available 

str = input("Entet a string: ")
letters = digits = sc = 0
for c in str:
	if c.isdigit():
		digits = digits + 1
	elif c.isalpha():
		letters = letters + 1
	else:
		sc = sc + 1

print("Count of letters is :",letters)
print("Count of digits is :",digits)
print("Count of special characters is :",sc)





