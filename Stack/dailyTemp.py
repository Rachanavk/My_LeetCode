# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #adding index and temperature[temp,index]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures): #i = index , t= temperature
# if stack is a list like [(73, 0), (74, 1), (75, 2)], then stack[-1] is (75, 2), and stack[-1][0] is 75
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)  
            
            stack.append([t,i])
        return res


            
            
        
