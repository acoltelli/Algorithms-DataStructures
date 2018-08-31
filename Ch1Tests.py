import unittest
import Ch1Solutions
import LinkedList
import random
import string 
import numpy



class Test(unittest.TestCase):

    def testisCharUnique(self):
    	assert Ch1Solutions.isCharUnique("too")== False
    	assert Ch1Solutions.isCharUnique("dhweur") == True 

    def testremoveChar(self):
    	assert Ch1Solutions.removeChar("otoooooooo")== "to"

    def testisAnagram(self):
    	assert Ch1Solutions.isAnagram("ab ac","ac ab")

    def testrotateMatrix(self):
    	assert Ch1Solutions.rotateMatrixClockwise([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    	assert Ch1Solutions.rotateMatrixClockwise([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[13,9,5,1], [14,10,6,2], [15,11,7,3], [16,12,8,4]]
    	assert Ch1Solutions.rotateMatrixClockwise([[0]]) == [[0]]
    	assert Ch1Solutions.rotateMatrixClockwise([[]]) == [[]]

    def testrotateMatrixCounterclockwise(self):
    	assert Ch1Solutions.rotateMatrixCounterclockwise([[1,2,3],[4,5,6],[7,8,9]]) == [[3,6,9],[2,5,8],[1,4,7]]

    def testsetZeros(self):
    	assert Ch1Solutions.setZeros([[1,0,1,1,4,5],[2,2,2,2,4,5],[3,3,3,0,4,5]]) == [[0,0,0,0,0,0],[2,0,2,0,4,5],[0,0,0,0,0,0]]
    	assert Ch1Solutions.setZeros([[1,0,1,1],[2,2,2,2],[3,3,3,0]]) == [[0, 0, 0, 0], [2, 0, 2, 0], [0, 0, 0, 0]]
    	assert Ch1Solutions.setZeros([[1,0,1,1],[2,2,0,2],[3,3,3,0]]) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    	assert Ch1Solutions.setZeros([[0]]) == [[0]]
    	assert Ch1Solutions.setZeros([[]]) == [[]]

    def testrepl(self):
    	assert Ch1Solutions.repl("we re") == "we%20re"

    def testisSubstring(self):
    	assert Ch1Solutions.isSubstring("rantoog", "too") == True 
    	assert Ch1Solutions.isSubstring("flabber","bur") == False 

    def testisRotation(self):
    	assert Ch1Solutions.isRotation("waterbottle","erbottlewa") == True 
    	assert Ch1Solutions.isRotation("paradigm","digmapra") == False 





if __name__ == "__main__":
    unittest.main()






        