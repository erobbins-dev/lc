class Solution:
   def romanToInt(self, s: str) -> int:
      map = {
         'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
      }

      i = len(s) - 1
      sum = 0
      while (i >= -0):
         curr = s[i]
         if i - 1 >= 0:
            prev = s[i-1]
         else:
            prev = ''
         if len(prev) > 0 and map[prev] < map[curr]:
            sum += map[curr] - map[prev]
            i -= 2
         else:
            sum += map[curr]
            i -= 1
      
      return sum

str = "IV"
sol = Solution()
print(sol.romanToInt(str))