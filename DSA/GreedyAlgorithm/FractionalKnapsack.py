"""
You have n items; the i-th item has value val[i] and weight wt[i].
A knapsack can carry at most capacity units of weight.
You may take any fraction of an item (i.e. split items).
Return the maximum total value that can be placed in the knapsack, rounded to exactly 6 decimal places.
"""

## Using the maximum ratio formula here
def fractional( val, wt, cap):
   #first is store everything in one array with the ratio 
   items =[]

   for i in range(len(val)):
      items.append([val[i]/wt[i], val[i], wt[i]])

   items.sort(reverse = True)

   max_value = 0.0
   
   for ratio,value, weight in items:
      
      if weight <= cap:
         max_value += value
         cap -= weight
      else:
         max_value+= ratio * cap
         break 
      
   return round(max_value, 6)

    
    

value = [40,10,60,40]
wt = [5,2,1,4]
cap = 10

maximumWeight = fractional(value,wt,cap)
print(maximumWeight)


