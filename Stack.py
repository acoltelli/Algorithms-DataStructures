import unittest
import random 

#produces stack with n elements(without using python append/pop functions)
class Stack:
    def __init__(self,n):
        self.size = n
        self.stack = [None] * self.size
        self.top = 0
    
    def __str__(self):
        return str(self.stack)

    def __getitem__(self, position):
        return self.stack[position]

    def __len__(self):
        var = [i for i in self.stack if i is not None]
        return len(var)
    
    def isFull(self):
        var = len([i for i in self.stack if i == None])
        if var ==0: return True 
        else: return False 

    def isEmpty(self):
        if self.stack == [None for i in range(len(self.stack))]:
            return True
        return False

    def push(self, data):
        if self.top >= self.size: 
            exit("Stack Overflow")
        self.stack[self.top] = data
        self.top += 1

    def pop(self):  #pops last value in stack 
        if self.top <= 0:
            exit("Stack Underflow")
        var = self.stack[self.top-1]
        self.stack[self.top-1]= None
        self.top -= 1        
        return var

    def popAt(self,index):  #pops value located at given index  
        if index >= self.top:
            exit("Index exceeds stack length")
        else: 
            var = self.stack[index]
            for i in range(index, self.top - 1):
                self.stack[i] = self.stack[i + 1]
            self.stack[self.top - 1] = None
            self.top -= 1
        return var 

    #CCI q 3.2
    def stackMin(self):
        var = self.stack[0]
        for i in self.stack:
            if i is not None and i < var:  
                var = i
        return var 

    # CCI q 3.6 
    def sortStack(self):   #insertion sort a stack 
       for i in range(1,len(self.stack)):
            current = self.stack[i]
            while i > 0 and self.stack[i-1] > current:       
                self.stack[i] = self.stack[i-1]
                i = i - 1
            self.stack[i] = current


###tests###

class Test(unittest.TestCase):   
    def testStack(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        bar = Stack(2)
        self.assertEqual(var.stack, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(bar.stack, [None, None])

    def testStackOverflow(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        with self.assertRaises(SystemExit): var.push(11)

    def testPop(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        self.assertEqual(var.pop(), 10)
        var.pop()
        self.assertEqual(var.stack, [1, 2, 3, 4, 5, 6, 7, 8, None, None])

    def testPush(self):
        var = Stack(10)
        for i in range(1,9):
            var.push(i)
        self.assertEqual(var.stack, [1, 2, 3, 4, 5, 6, 7, 8, None, None])
        var.push(9)
        self.assertEqual(var.stack, [1, 2, 3, 4, 5, 6, 7, 8, 9, None])
        
    def testStackUnderflow(self):
        var = Stack(1)
        with self.assertRaises(SystemExit): var.pop()

    def testPopAt(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        self.assertEqual(var.popAt(0), 1) 
        self.assertEqual(var.stack, [2, 3, 4, 5, 6, 7, 8, 9, 10, None])
        var.push(100)
        self.assertEqual(var.stack, [2, 3, 4, 5, 6, 7, 8, 9, 10, 100])
        self.assertEqual(var.popAt(9), 100) 
        self.assertEqual(var.pop(), 10)
        self.assertEqual(var.stack, [2, 3, 4, 5, 6, 7, 8, 9, None, None])

    def testOutOfRange(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        with self.assertRaises(SystemExit): var.popAt(11)

    def testStackMin(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        self.assertEqual(var.stackMin(), 1)
        bar = Stack(2)
        self.assertEqual(bar.stackMin(), None)
        var.pop()
        self.assertEqual(var.stackMin(), 1)  

    def testSortStack(self):
        var = Stack(5)
        var.push(5)
        var.push(4)
        var.push(3)
        var.push(2)
        var.push(1)
        var.sortStack()
        self.assertEqual(var.stack, [1, 2, 3, 4, 5])
        
        bar = Stack(10)
        for i in range(0,10):
            j = random.randint(1,10)
            bar.push(j)
        bar.sortStack() 
        self.assertEqual(bar.stack, sorted(bar)) #test against sorted function 


if __name__ == "__main__":
    unittest.main()



