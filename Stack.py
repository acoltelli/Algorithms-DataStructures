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

    # def __len__(self):
    #     var = [i for i in self.stack if i is not None]
    #     return len(var)
    
    # def isFull(self):
    #     var = len([i for i in self.stack if i == None])
    #     if var ==0: return True 
    #     else: return False 

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

    def testOutOfRange(self):
        var = Stack(10)
        for i in range(1,11):
            var.push(i)
        with self.assertRaises(SystemExit): var.popAt(11)


if __name__ == "__main__":
    unittest.main()



