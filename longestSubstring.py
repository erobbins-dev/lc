#!/usr/bin/python3
from collections import deque

class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:

      chrMap = {}
      dq = deque()
      maxStr = 0
      front = 0

      for i, ltr in enumerate(s):
         if ltr in chrMap:
            # do something
            while dq[0] != ltr:
               char = dq.popleft()
               del(chrMap[char])
            dq.popleft()

         dq.append(ltr)
         currLen = len(dq)
         if currLen > maxStr:
            maxStr = currLen
         chrMap[ltr] = dq[0]
      
      return maxStr

str = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(str))