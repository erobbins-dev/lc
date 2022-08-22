#!/usr/bin/python3

class Solution:
   def removeElement(self, nums: list[int], val: int) -> int:
      oLen = len(nums)
      tailNdx = oLen - 1
      i = 0
      while (i <= tailNdx):
         while (nums[i] == val and i <= tailNdx):
            nums[i] = nums[tailNdx]
            tailNdx -= 1
         i += 1
      return tailNdx + 1

nums = []
val = 2

sol = Solution()

print(sol.removeElement(nums, val))