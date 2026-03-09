# import gzip
# with gzip.open(path, 'rt') as fp:
	# for lin in fp:
	#	print(line, end='')
		
# w = 10
# s = 1
# for i in range(0, len(seq) -w +1, s):
#	subseq = seq[i:i+w]
	
s = {'A', 'C', 'G'}
print(s)

s.add('T')
print(s)

s.add('A')
print(s)

# print(s[2])

d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

# print(d['rat']) creates an error

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k,'says', v)

for thing in d.items(): print(thing[0], thing[1])

print(d.keys(), d.values(), list(d.values()))

kdtable = {'I': 4.5, 'V': 4.2, 'L': 3.8, 'F': 2.8, 'C': 2.5, 'M':1.9, 'A': 1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5}
def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)
	
print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][3])

d = ['hello', (3.14, 'pi'), [-1, 0, 1], {'year': 2000, 'month': 7}]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])

oligo = {'Name': 'S0116', 'Length': 18, 'Sequence': 'ATTTAGGTGACACTATAG', 'Description': 'SP6 promoter sequencing primer'}

catalog = []
catalog.append(oligo)

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
	
kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1
	
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)

truc = {'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
'numbers':[1.09, 2.72, 3.14], 'is_complete': False,}
print(json.dumps(truc, indent=4))

