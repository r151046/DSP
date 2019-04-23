def m_mul(a,b,c,d):
	if(b!=c):
		print "matrix multiplication is not possible"
	else:
		#A=[[0,0,0],[0,0,0]]
		#B=[[0,0],[0,0],[0,0]]
		temp=[0]
		temp1=temp*b
		A=[temp1,temp1]
		temp2=temp*d
		B=[temp2,temp2,temp2]
		for i in range(0,a):
			A[i]=input("Enter row of matrix1 in list form:")
		for j in range(0,c):
			B[j]=input("Enter row of matrix2 i list form:")
		for i in range(0,len(A)):
			print A[i]
		for l in range(0,len(B)):
			print B[l]
		z=[[0,0],[0,0]]
		for x in range(0,len(A)):
			for y in range(len(B[0])):
				for w in range(len(B)):
					z[x][y] += A[x][w] * B[w][y]
		for r in z:
			print r

a=input("Enter number of rows for matrix1:");
b=input("Enter number of columns for matrix1:")
c=input("Enter number of rows for matrix2:");
d=input("Enter number of columns for matrix2:")
m_mul(a,b,c,d)