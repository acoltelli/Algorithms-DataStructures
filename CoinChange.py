import unittest


# recursive sol
# find the number of ways to sum values in arr to get n
def coinChange(arr, len, n):
    if n == 0:
        return 1  # n=0, include 0 values- 1 sol
    if n < 0 or (len == 0 and n >= 1):
        return 0
    # sol is sum of solutions not including last term in arr + solutions including last term
    return coinChange(arr, len - 1, n) + coinChange(arr, len, n - arr[len - 1])


# recusive sol without using memoization
# compute the fewest number of coins you need to sum to n
def coinChange_(arr, n):
    arr = [i for i in arr if i <= n]  # eliminate coins of value greater than n
    minCoins = n
    if n in arr:
        return 1  # base case where there is a coin in arr equal to n
    else:
        for i in arr:
            numCoins = 1 + coinChange_(arr, n - i)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins


# dynamic programming sol
# compute the fewest number of coins you need to sum to n
def coinChangeDP(arr, n):
    dp = [0] + [
        n + 1
    ] * n  # first index set to 0 because there is 0 ways to sum to 0 from arr
    for i in range(1, n + 1):
        for j in arr:
            if i >= j:
                dp[i] = min(dp[i], dp[i - j] + 1)
    if dp[n] == n + 1:
        return None  # if n cannot be made up of any combination in arr
    return dp[n]


class Test(unittest.TestCase):
    def testCoinChange(self):
        self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 4), 4)
        self.assertEqual(coinChange([1, 2], len([1, 2]), 4), 3)
        self.assertEqual(coinChange([1, 2, 7], len([1, 2, 7]), 4), 3)
        self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 5), 5)
        self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), 0), 1)
        self.assertEqual(coinChange([1, 2, 3], len([1, 2, 3]), -5), 0)
        self.assertEqual(coinChange([], len([]), 5), 0)

    def testCoinChangeDP(self):
        self.assertEqual(coinChangeDP([1, 2, 5], 11), 3)
        self.assertEqual(coinChangeDP([1, 5, 10], 12), 3)
        self.assertEqual(coinChangeDP([2, 5, 10], 12), 2)

        self.assertEqual(coinChangeDP([2], 3), None)
        self.assertEqual(coinChangeDP([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
