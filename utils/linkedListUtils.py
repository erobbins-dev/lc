#!/usr/bin/python3

class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def generate(vals):
   n = len(vals)
   if n == 0: 
      return None
   
   def getNextNode(i):
      if i == n:
         return None
      node = ListNode(vals[i], getNextNode(i+1))
      return node
   
   return getNextNode(0)

def traverse(head):
   vals = []
   if head:
      while head:
         vals.append(head.val)
         head = head.next
   return vals