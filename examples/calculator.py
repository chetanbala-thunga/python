calc_on = 1
def addition():
    print("Adding two values")	
    first = float(raw_input('What is your first number?'))
    second = float(raw_input('What is your second number?'))
    print(first + second)

def subtraction():
    print("Substracting two values")
    first = float(raw_input('What is your first number?'))
    second = float(raw_input('What is your second number?'))
    print(first - second) 

def multiplication():
    print("Multiplying two values")
    first = float(raw_input('What is your first number?'))
    second = float(raw_input('What is your second number?'))
    print(first * second)

def division():
    print("Division of two values")
    first = float(raw_input('What is your first number?'))
    second = float(raw_input('What is your second number?'))
    print(first / second)

def modulo():
    print("Remainder of two values after division")
    first = float(raw_input('What is your first number?'))
    second =  float(raw_input('What is your second number?'))
    print(first % second)

def count_to_ten():
     for number in range (1,11):
	 print(number)

def quit():
    global calc_on
    calc_on = 0

def calc_run():
    op = raw_input('add, subtract, multiply, divide, modulo, or ten? ')
    if op == 'add':
	addition()
    elif op == 'subtract':
	subtraction()
    elif op == 'multiply':
	multiplication()
    elif op == 'divide':
    	division()
    elif op == 'modulo':
	modulo()
    elif op == 'ten':
	count_to_ten()
    else:
	quit()

while calc_on == 1:
	calc_run()
