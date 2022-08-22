#!/usr/bin/python3

def maxProfit(prices):

   numDays = len(prices)
   futureMax = []
   maxPrice = 0
   maxDay = 0
   minPrice = 999999
   minDay = numDays + 1
   maxProfit = 0

   for i, price in enumerate(prices[::-1]):
      if price > maxPrice:
         maxPrice = price
         #maxDay = numDays - 1 - i
      #futureMax.append((currMax, maxDay))

      if maxPrice - price > maxProfit:
         maxProfit = maxPrice - price

      print(maxProfit)

   return maxProfit


prices = [7,1,5,3,6,4]
final = maxProfit(prices)
print(f'Max profit: {final}')