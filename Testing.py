
#calculator simple

def first_john_codes():
	first_num = 0
	second_num = 0
	answer = 0
	print ("Type in first number to the calculator")	
	first_num = float(input(""))
	print ("Type in the operator")
	operator_1 = input("")
	print ("Type in the second number to the calculator")
	second_num = float(input(""))
	if operator_1 == "+":
		answer = first_num + second_num
		print (answer)
	elif operator_1 == "-":
		answer = first_num - second_num
		print (answer)
	elif operator_1 == "/":
		answer = first_num // second_num
		print (answer)
	elif operator_1 == "*":
		answer = first_num * second_num
		print (answer)
	





def main():
	first_john_codes()

if __name__ == "__main__":
	main()
