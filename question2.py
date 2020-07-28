import numpy as np
#getting number of rows of coefficient matrix
m = int(input("give number of rows: "))
#getting number of columns of coefficient matrix
n = int(input("give number of columns: "))
#we declare an empty list to be able to append other lists to it
a = []
for i in range(m):
    #getting all the rows note that rows start from zero
    #for inputting the rows you should write the numbers of row one after another with a space between
    print("give row %d "%(i))
    row = input()
    #casting all the numbers to float because we can't work with strings 
    row2 = row.split()
    row2 = [float(i) for i in row2]
    #adding each row to a list
    a.append(row2)
#creating the matrix using numpy
A = np.array(a)
print('\nthe matrix:\n',A)
ARank = np.linalg.matrix_rank(A)
#from a theorem rank+dimNull = n
dimNullA = n - ARank
print('dimention af null space of A: ',dimNullA)
print('rank of A: ',ARank)