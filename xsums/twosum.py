#!/usr/bin/python3


class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
      hm = {}
      for i, k in enumerate(nums):
         if target-k in hm:
            return [i, hm[target-k]]
         hm[k] = i

nums = [3,2,4]
target = 6

sol = Solution()

print(sol.twoSum(nums, target))


# class Solution:
#    def twoSum(self, nums: list[int], target: int) -> list[int]:
#       indexedNums = []
#       for i, num in enumerate(nums):
#          indexedNums.append((num, i))

#       indexedNums = sorted(indexedNums, key=lambda num: num[0])
#       l = 0
#       r = len(indexedNums) - 1
#       while (l < r):
#          sum = indexedNums[l][0] + indexedNums[r][0]
#          if sum == target:
#             return [indexedNums[l][1], indexedNums[r][1]]
#          if sum > target:
#             r -= 1
#          if sum < target:
#             l += 1
