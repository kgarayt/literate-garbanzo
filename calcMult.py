import sys

def mult(a,b):
	print a*b*2
	
if __name__ == '__main__':
	print "Here the result :"
	if len(sys.argv)==3:
		mult(int(sys.argv[1]),int(sys.argv[2]))
	else:
		print "error"