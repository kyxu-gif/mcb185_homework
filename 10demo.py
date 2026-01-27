# 10demo.py by kaylee_xu

print("hello, again") # greeting

print(1.5e-2) # scientific notation

print(1 + 1) # addition
print(1 - 1) # subtraction
print(2 * 2) # multiplication
print(1 / 2) # division
print(2 ** 3) # exponentiation
print(5 // 2) # integer divide
print(5 % 2) # remainder
print (5 * (2 + 1)) # precedence

print(pow(2, 3)) # x to power of y
print(math.pow(2, 3))
print(math.sqrt(2)) # square root of x
print(math.log(2)) # x in log base e

# hypotenuse c given sides a and b
a = 3	# side of triangle
b = 4 	# side of triangle
c = math.sqrt(a**2 + b**2) 	# hypotenuse
print(c)

print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ', end='!\n')
# \n means "newline"

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
# a and b are "parameters" or "arguments" of the function

hyp = pythagoras (3, 4)
print(hyp)

hyp = pythagoras(3, 4)
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(3, 4))
