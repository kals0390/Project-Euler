'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.'''

def fn():
	sumnum = 0
	sqsum = 0
	for i in xrange(1,101):
		sumnum+= i
		sqsum += (i**2)

	sqsumnum = (sumnum**2)
	diff = sqsumnum - sqsum
	print diff

















