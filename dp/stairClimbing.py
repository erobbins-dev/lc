#!/usr/bin/python3
import numpy as np

class Solution:
   def climbStairs(self, n: int) -> int:
      # dp solution:
      
      if (n == 1):
         return 1

      memos = [0, 1, 2]

      for i in range(3, n+1):
         memos.append(memos[i-1] + memos[i-2])
      
      return memos[n]

      # recursive w/ memoization solution:
      # memos = {}

      # def climb(stepsLeft: int) -> int:
      #    if stepsLeft == -1:
      #       return 0
      #    if stepsLeft == 0:
      #       return 1
      #    if stepsLeft in memos:
      #       return memos[stepsLeft]
         
      #    options = climb(stepsLeft-1) + climb(stepsLeft-2)
      #    memos[stepsLeft] = options
      #    return options

      # return climb(n)

n = 1
sol = Solution()
print(sol.climbStairs(n))