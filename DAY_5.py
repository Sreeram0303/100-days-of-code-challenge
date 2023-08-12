#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index. 

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created. 
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #overriden
}
print(thisdict)

#length 
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Accessing 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

#Updating the values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) 
thisdict.update({"year": 2020})
print(thisdict)

#removing items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")#removes selected item
print(thisdict)
print(thisdict.popitem()) #removes last item
del thisdict["brand"] #delete the specific key
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #clears the dict
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print the keys
for x in thisdict:
  print(x) 
for x in thisdict.keys():
  print(x)
#prints values
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
#print items
for x, y in thisdict.items():
  print(x, y)

#to copy
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#Methods
"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""
#Problem_1 on Hashing
from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    n = len(v)
    HM = {}
    for i in range(n):
        if v[i] in HM:
            HM[v[i]] += 1
        else:
            HM[v[i]] = 1
    
    mx_freq = -1  # Initialize max frequency to a value lower than 0
    mn_freq = float('inf')  # Initialize min frequency to positive infinity
    mx_el = None
    mn_el = None
    
    for x, y in HM.items():
        if y > mx_freq or (y == mx_freq and x < mx_el):
            mx_freq = y
            mx_el = x
        if y < mn_freq or (y == mn_freq and x < mn_el):
            mn_freq = y
            mn_el = x
    
    return mx_el, mn_el
#Problem_2
from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):

    hsh = [0]*max(n+1,m+1)
    for i in range(n):
        hsh[edges[i]] += 1
    ans = []
    for i in range(1,n+1):
        ans.append(hsh[i])
    return ans

#Sorting
#selection sort
n = 5
lst = [5,4,3,2,1]
for i in range(n-1):
    mn = i
    for j in range(i+1,n):
       if lst[j] < lst[mn]:
          mn = j
    if min != i:
       temp = lst[i]
       lst[i] = lst[mn]
       lst[mn] = temp     
print(lst)
#Bubble sort
n = 5
lst = [5,4,3,2,1]
for i in range(n-1,-1,-1):
   for j in range(0,i):
      if lst[j] > lst[j+1]:
         temp = lst[j]
         lst[j] = lst[j+1]
         lst[j+1] = temp
print(lst)
#Insertion sort
n = 5
lst = [5,4,3,2,1]
for i in range(1,n):
   k = i
   while k > 0 and lst[k] < lst[k-1]:
      temp = lst[k]
      lst[k] = lst[k-1]
      lst[k-1] = temp
      k -= 1
print(lst)
      
       
      




