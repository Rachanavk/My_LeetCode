#3Sum
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #Go through each index and value in nums
        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i-1] ==a:
                continue
            #create two pointers l and r. [-3,-3,1,2,3,4]. a is at -3 and l is at -3 and r is at 4
            l,r = i+1,len(nums)-1
            # ensure l is always < r
            while(l<r):
            #calculate sum= 0
                sum = a+nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    #[-3,-3,-3,1,2,4] l was at -3. when it incremenets its -3 again. keept doing until it does not have -3
                    #to remove duplicates check if current value and previous avlue is same and increment it by 1
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
        return res
