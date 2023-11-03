#!/usr/bin/env python
# coding: utf-8

# # Question 1
# In a jupyter notebook solve the following question. Please upload the notebook to GitHub and provide the link submission box below.
# 
#  
# 
# __int()__: Constructor that takes as input a pair of Point objects that represent the ends points of the line segment
# 
# Length():: returns the length if the segment 
# 
# Slope() returns the slope of the segment of none if the slope is unbounded 
# 
#  
# 
# >>> p1 = Point(3,4)
# 
# >>> p2 = Point()
# 
# >>> s = Segment(p1,p2)
# 
# >>> s.length()
# 
# 5.0
# 
# >>> s.slope()
# 
# 0.75

# In[4]:


import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return math.sqrt(dx**2 + dy**2)  # Fixing the exponentiation operator here

    def slope(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y

        if dx == 0:
            return None
        return dy / dx

# Usage
p1 = Point(4, 3)  # Create a Point with x=4 and y=3
p2 = Point()      # Create a Point with default values (x=0, y=0)
s = Segment(p1, p2)

print(s.length())  # this should print 5.0
print(s.slope())   # this should print 0.75


# In[ ]:




