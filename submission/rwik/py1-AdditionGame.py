def getMaximumPoints(A, B, C, N):
	final_points = 0
	for i in range(0,N):
		final_points += max(A,B,C)
		x = max(A,B,C)
		if x >=1:
			x -= 1
		else:
			x = x
		if max(A,B,C) is A:
			A = x
		elif max(A,B,C) is B:
			B = x
		else:
			C = x
	print "The maximum points Fox Ciel can get from these numbers for",N,"iterations is",final_points
A = input("Enter first number between 1 and 50! ")
B = input("Enter second number between 1 and 50! ")
C = input("Enter third number between 1 and 50! ")
N = input("Enter the number of times Ciel repeats the operation between 1 and 150! ")
if A not in range (1,51) or B not in range(1,51) or C not in range(1,51) or N not in range (1,151):
	print "Invalid inputs. Game over..."
	exit(0)
else:
	getMaximumPoints(A,B,C,N)