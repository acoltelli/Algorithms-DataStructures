import unittest

#find the number of ways to sum values in arr to get n 
def coinChange(arr, len, n): 
    if n == 0: 
        return 1  #n=0, include 0 values- 1 sol
    if n < 0 or (len == 0 and n >= 1): 
        return 0 
    # sol is sum of solutions not including last term in arr, plus solutions including last term
    return coinChange(arr, len - 1, n) + coinChange(arr, len, n - arr[len-1]); 
  




class Test(unittest.TestCase): 
	def testCoinChange(self):
		self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 4), 4)
		self.assertEqual(coinChange([1, 2], len([1, 2]), 4), 3)
		self.assertEqual(coinChange([1, 2, 7], len([1, 2, 7]), 4), 3)
		self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 5), 5)
		self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 0), 1)
		self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), -5), 0)
		self.assertEqual(coinChange([], len([]), 5), 0)








if __name__ == "__main__":
    unittest.main()
