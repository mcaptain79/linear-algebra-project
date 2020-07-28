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
coefficientMatrix = np.array(a)
#getting b matix
b = input("give b: ")
#converting b members to float
b2 = b.split()
b2 = [float(i) for i in b2]
#creating b matrix
bMatrix = np.vstack(b2)
#here is the algorithm for making augmented matrix
"""first we declare an empty list in order to be able put rows sequentially in it
then we declare another list to put rows in a list form
"""
empty = []
augmented = []
for i in range(m):
    for j in range(n):
        empty.append(coefficientMatrix[i][j])
    empty.append(bMatrix[i][0])
    augmented.append(empty)
    empty = []
#now we have made our augmented matrix
augmentedMatrix = np.array(augmented)
print("\naugmented matrix:\n",augmentedMatrix)
#we make an identity matrix in order to be able to make elementry matrix
Im = np.identity(m)
elementry = np.identity(m)
"""this function change two rows of a marix by receiving 3 elements
first we receive row1 and then we receive row2 and finally we receive
the matrix and we return the changed matrix
"""
def changeRow(r1,r2,I):
    I[[r1,r2]] = I[[r2,r1]]
    return I
#this function adds m*row1 to row2
def coefficientRow(m,r1,r2,I):
    I[r2] = m*I[r1]+I[r2]
    return I
print('---------------------------------------------')
"""this is an algorithm for finding echelon form but it is not complete
and we should make this with the correct order
"""
for i in range(m):
    for j in range(n):
        if augmentedMatrix[i,j] != 0:
            for counter in range(m):
                if counter != i:
                    r = -(augmentedMatrix[counter,j]/augmentedMatrix[i,j])
                    augmentedMatrix[counter] = r*augmentedMatrix[i]+augmentedMatrix[counter]
                    augmentedMatrix = np.round(augmentedMatrix,2)
                    #lines below show step by step and also show elementry matrix
                    elementry = coefficientRow(r, i, counter, elementry)
                    elementry = np.round(elementry,2)
                    print('elemetry:\n',elementry)
                    print('matrix:\n',augmentedMatrix)
                    elementry = coefficientRow(-r, i, counter, elementry)
                    #print('---------------------------------------------')
            break    
#in this alogorithm we make the echelon form in correct order
jList = []
count = 0
for i in range(n):
    for j in range(m):
        if augmentedMatrix[j,i] != 0:
            if j in jList:
                break
            else:
                jList.append(count)
                augmentedMatrix[[count,j]] = augmentedMatrix[[j,count]]
                count = count+1
                #lines below show program step by step and elementry matrix
                #elementry[[count,j]] = elementry[[j,count]]
                #print('elementy:\n',elementry)
                #print('matrix:\n',augmentedMatrix)
                #elementry[[j,count]] = elementry[[count,j]]
                #print('---------------------------------------------')

#in this algorithm we made the first non zero member of each column one by division
for i in range(m):
    for j in range(m):
        if augmentedMatrix[i,j] != 0:
            r = augmentedMatrix[i,j]
            augmentedMatrix[i] = (1/r)*augmentedMatrix[i]
            #lines below show program step by step and elementry matrix
            #elementry[i] = (1/r)*elementry[i]
            #print('elementry:\n',elementry)
            #print('matrix:\n',augmentedMatrix)
            #print('---------------------------------------------')
            #elementry[i] = (r)*elementry[i]
            break
augmentedMatrix = np.round(augmentedMatrix,2)
print("echelon form:\n",augmentedMatrix)
print('--------------------------------------------')
zeroArray = []
#at first we consider we have a solution
hasSolution = True
for i in range(n):
    zeroArray.append(0)
zeroNumpy = np.array(zeroArray)
#in this case we check if our equation is inconsistent or not
for i in range(m):
    if (augmentedMatrix[i,0:n] == zeroNumpy).all() and augmentedMatrix[i,n] != 0:
        hasSolution = False
        break
#if we have a solution we print it if not we print inconsistent
#if we hava a unique solution we print it if we have infinity solutions we print one of them
if hasSolution:
    c = np.linalg.lstsq(coefficientMatrix,bMatrix,None)
    x = np.round(c[0],2)
    print('solution:\n',x)
else:
    print('inconsistent')









