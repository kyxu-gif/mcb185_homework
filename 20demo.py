s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
print('hey "dude" don\'t tell me what to do')

print(s.upper())
print(s)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

import math
print(f'{math.pi}') 			# does nothing special
print(f'{math.pi:.3f}') 		# 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}') 	# exponent notation
print(f'{"hello world":>20}') 	# right justify with space filler
print (f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')			# left justify

print(s.upper())
print(s) 

print('{}{:.3f}'.format('str.format', math.pi))

print('%s %.3f' % ('printf', math.pi))

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5]) 		# both ABCDE
print(s[5:len(s)], s[5:]) 	# both FGHIJ

print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'
for i in range(0,len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	
tax = ('Homo', 'sapiens', 9606) 	# construct tuple
print(tax) 							# note parentheses in output

print(tax[0]) 		# index
print(tax[::-1])	# slice

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append('eggs')
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day		to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('indexG?', alph.index('G'))
# print('index Z?', alph.index('Z'))	creates an error

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Practice Problems
# Write a function that returns minimum value of a list.
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
print(minimum([2, 4, 6, 8]))

# Write a function that returns both minimum and maximum values of a list
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
print(minmax([2,4,6,8]))

# Write a function that returns the mean values in a list
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
print(mean([2, 4, 6, 8]))

# Write a function that computes the entropy of a probability distribution
import math
def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h	

print(entropy([0.2, 0.3, 0.5]))

# Write a function that computes Kullback-Leiber distance between two sets of probability distributions
def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log(p / q)
	return d
p1 = [0.1, 0.2, 0.3, 0.4]
p2 = (0.4, 0.3, 0.2, 0.1)
print(dkl(p1, p2))
