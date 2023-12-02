# Container with most water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.
class Solution:
  def maxArea(self, height: List[int]) -> int:
    a,b = 0,len(height)-1
    maxArea = 0
    while(a<b):
      if height[a] <height[b]:
        maxArea = max(maxArea,height[a]*b-a)
        a+=1
      else:
        maxArea = max(maxArea,height[b]*b-a)
        b+=1
    return maxArea
