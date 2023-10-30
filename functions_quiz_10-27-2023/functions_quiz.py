def simple_calculator(num1: int, num2:int, operation: str):
	if operation == 'add':
		return num1+num2
	if operation == 'subtract':
		return num1-num2

argum = input("enter num1, num2, and operation seperated by spaces")
argum = argum.split(" ")
print(simple_calculator(int(argum[0]),int(argum[1]),str(argum[2])))

def CandyDispenser(num: int):
	while num > 0:
		print(f"you can have {num} pieces of candy!")
		type = input("would you like snicker or mnm?          ")
		if type == "snickers":
			print("ok, heres a snickers")
		else:
			print("ok, heres an mnm")
		num-=1
		
CandyDispenser(5)

def OobaAdder():
	word = input("enter a word: ")
	print(f"{word}ooba")

OobaAdder()