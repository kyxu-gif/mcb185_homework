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

# Block Structure
def pythagoras(a, b): return math.sqrt (a**2 + b**2)

# Function Practice
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2
def square_area(w, h): return w * h
def circle_circumference(r): return 2 * math.pi * r
def square_volume(w,h): return w**2 * h
def c_to_f(c):
	return c / 9 * 5 + 32
print(c_to_f(0))
print(c_to_f(100))
print(c_to_f(-40))

# Strings
s = 'hello world'
print(s, type(s))

# Conditionals
a = 2
b = 2
if a == b:
	print('a equals b') 	# indented bc of block structure
print(a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False
	
print(is_even(2))
print(is_even(3))

# Boolean
c = a == b
print(c)
print(type(c))

# if-elif-else
if a < b:  	print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

# Boolean Chains
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# Floating Point Warning
a = 0.3
b = 0.1 * 3
if 	 a < b: print('a < b'))
elif a > b: print('a > b')
else:		print('a == b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough') 

# String Comparison
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# Mismatched Type Error
a = 1
s = 'G'
if a < s: print('a < s')

# None Type
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))

# Practice
import math 

def is_integer(x):
	r = x % 1
	return r
	if math.isclose(0, r): return True
	else: return False
	
print(is_integer(3.0))

def max_of_three(a, b, c)
	if a > b: return a
	elif b > c: return b
	else: return c 