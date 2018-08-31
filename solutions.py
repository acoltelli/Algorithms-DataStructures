import random
import string 

length= 12
randomString=''.join(random.choice(string.ascii_letters) for i in range(length))
randomString2=''.join(random.choice(string.ascii_letters) for i in range(length))


# CCI q1.1
def isCharUnique(str):
	var=0
	for i in str:
		var+=1
		count = str.count(i)
		if count>1:
			return False
			break
		elif var>=len(str):
			return True 
		
#CCI q1.3
def removeChar(str):
	x=0
	y=len(str)
	for i in str:
		x+=1
		count = str.count(i)
		if count>1:
			var=str.replace(i, '',count-1)
			str=var 
		if x==y:
			return str 


#CCI q1.4
def isAnagram(s1,s2):
	a=list(s1)
	b=list(s2)
	a.sort()
	b.sort()
	if a==b:
		return True 
	else:
		return False 
	
#CCI q1.5
def repl_(str):
    var=str.replace(' ', '%20')
    str=var
    return var


def repl(str):
    lst = list(str)
    temp = list()
    for i in lst: 
        if i == ' ':    
            i = '%20'
            temp.append(i)
        else:
            temp.append(i)
    return ''.join(temp)



#CCI q1.6
#rotate NxN matrix 90 degrees, clockwise  
def rotateMatrixClockwise(originalMatrix):
    newMatrix = [i[:] for i in originalMatrix]
    length = len(originalMatrix[0])
           
    for row in range(0,length):
        for column in range(0,length):
            newMatrix[column][length-(row+1)] = originalMatrix[row][column] 
    return newMatrix

#rotate 90 degrees, counterclockwise 
def rotateMatrixCounterclockwise(originalMatrix):
    newMatrix = [i[:] for i in originalMatrix]
    length = len(originalMatrix[0])
           
    for row in range(0,length):
        for column in range(0,length):
            newMatrix[length-(column+1)][row] = originalMatrix[row][column]
    return newMatrix
    	
# CCI 1.7 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0 
#TODO: refactor 
zeros=[]
def locateZeros(matrix):
    for row, rowElements in enumerate(matrix):
        for column, colElements in enumerate(rowElements):
            if colElements == 0:
                    zeros.append((row,column))
    return zeros                

def setZeros(matrix):
    zeros=locateZeros(matrix)
    for row, rowElements in enumerate(matrix):
        for column, colElements in enumerate(rowElements):
            if row in (i[0] for i in zeros) or column in (i[1] for i in zeros):
                matrix[row][column] = 0
    return matrix



#CCI q1.8
def isSubstring(str1, str2):
	var=str1.find(str2)
#find: index if found, -1 otherwise
	if var>-1:
		return True
	else:
		return False


def isRotation(st1,st2):
		str=st1+st1
		if isSubstring(str,st2)==True:
			return True 
		elif isSubstring(str,st2)==False:
			return False 







