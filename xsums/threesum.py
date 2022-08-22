class Solution:
   def threeSum(self, nums: list[int]) -> list[int]:
      hm = {}
      ansSet = set()
      for i, k in enumerate(nums):
         hm[k] = i
      for i in range(0, len(nums)):
         for j in range(i+1, len(nums)):
            complement = 0 - (nums[i] + nums[j])
            if complement in hm and hm[complement] is not i and hm[complement] is not j:
               tuparr = [nums[i], nums[j], complement]
               tuparr.sort()
               ansSet.add((tuparr[0], tuparr[1], tuparr[2]))
      return [[a, b, c] for (a, b, c) in ansSet]
   
nums = [0,1,1]
sol = Solution()

print(sol.threeSum(nums))