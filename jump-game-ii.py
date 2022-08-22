#!/usr/bin/python3
from typing import List

class Solution:
   def jump(self, nums: List[int]) -> int:
      target_space = len(nums) - 1
      if (target_space == 0):
         return 0
      
      pos = 0
      total_jumps = 0

      while True:
         jump_dist = nums[pos]
         if pos + jump_dist >= target_space:
            return total_jumps + 1

         max_possible_from_next = 0
         final_next_space = pos + jump_dist

         while jump_dist > 0:
            next_space = pos + jump_dist
            if jump_dist + nums[next_space] > max_possible_from_next:
               max_possible_from_next = jump_dist + nums[next_space]
               final_next_space = next_space
            jump_dist -= 1

         pos = final_next_space
         total_jumps += 1
      
sol = Solution()

nums = [0]
print(sol.jump(nums))