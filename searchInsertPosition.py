#!/usr/bin/python3

class Solution:
   def searchInsert(self, nums: list[int], target: int) -> int:
      l = 0
      r = len(nums) - 1
      while (l <= r):
         mid = (r + l) // 2
         if target == nums[mid]:
            return mid
         if target < nums[mid]:
            r = mid - 1
         if target > nums[mid]:
            l = mid + 1
      return l

nums = [0,1]
target = 2
sol = Solution()

print(sol.searchInsert(nums, target))
