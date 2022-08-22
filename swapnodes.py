#!/usr/bin/python3
import utils.linkedListUtils as ll

def swapPairs(head):

   def recursiveSwap(first, second):
      # end of the list - return value may be single node (if length is odd) or null
      if not (first and second):
         return first

      # define the next pair to swap it more easily
      firstNextPair = second.next
      secondNextPair = firstNextPair.next if firstNextPair else None

      # swap current pair, point next to recursively-generated remainder of list
      # return second as it is new head that prev should point to
      second.next = first
      temp = recursiveSwap(firstNextPair, secondNextPair)
      first.next = temp
      return second

   # do a quick swap of the first pair, save the new head as final return val, then swap away
   if not head or not head.next:
      return head
   finalHead = head.next
   recursiveSwap(head, head.next)
      
   return finalHead

vals = [1, 2]
test = ll.generate(vals)
ans = swapPairs(test)
print(ll.traverse(ans))


