#!/usr/bin/python3


from lib2to3.pytree import convert


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   def addTwoNumbers(self, l1, l2):

      def convert(node):
         i = 0
         num = 0
         while node:
            num += node.val * 10**i
            i += 1
            node = node.next
         return num

      n1 = convert(l1)
      n2 = convert(l2)
      sum = n1 + n2
      i = 1
      node = ListNode(sum % 10)
      origNode = node
      sum = sum // 10
      while sum > 0:
         # i += 1
         node.next = ListNode(sum % 10)
         node = node.next
         sum = sum // 10
      
      return origNode

n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))

sol = Solution()

print(sol.addTwoNumbers(n1, n2))