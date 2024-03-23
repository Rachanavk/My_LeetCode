# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Logic-> 1. Create an empty dict.
# 2. Go through each index and value and find the difference of val with the target. 
# 3. If the difference is already in the dict then return the value at the particular index along with the current index. 
# 4. Else assign the current index to the point to the value
# Example- i=0 val = 2 diff = 7 
# 2 not in prev_val->Add prev_val[2]=0 Table 0:2
# now i=1 val = 7 diff = 2
# 2 is in prev_val=> prev_val[2]=0 and i=1   [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_val = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in prev_val:
                return [prev_val[diff],i]
            prev_val[val]=i
