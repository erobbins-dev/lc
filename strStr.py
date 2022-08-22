#!/usr/bin/python3

class Solution:
   def strStr(self, haystack: str, needle: str) -> int:
      n_size = len(needle)
      if n_size == 0:
         return 0
      h_size = len(haystack)

      f_ndx = -1
      h_ndx = 0
      h_tmp_ndx = 0
      n_ndx = 0

      while h_ndx < h_size:
         if haystack[h_ndx] == needle[0]:
            h_tmp_ndx = h_ndx
            f_ndx = h_ndx
            n_ndx = 0
         while haystack[h_tmp_ndx] == needle[n_ndx]:
            h_tmp_ndx += 1
            n_ndx += 1
            if n_ndx == n_size:
               return f_ndx
            if h_tmp_ndx == h_size:
               return -1

         h_ndx += 1

      return -1

sol = Solution()

haystack = 'mississippi'
needle = 'issip'

print(sol.strStr(haystack, needle))