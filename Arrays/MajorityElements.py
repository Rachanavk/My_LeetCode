# Example 1:

# Input: nums = [3,2,3]
# Output: 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i]=0
            count[i]+=1

            if count[i]>len(nums)//2:
                return i
