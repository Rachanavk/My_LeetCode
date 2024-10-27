# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

Logic:
# 1. result = size same as input size
# 2. prefix = 1
# 3. go through all the elements in ascending order
# 4. res[i] = prefix: The result at each index i is set to the cumulative prefix value, which is the product of all numbers to the left of I.
# 5.prefix *= nums[i]: The prefix variable is then updated by multiplying it with nums[i], so it accumulates the product of all elements up to the next index.
# 6. 2nd loop goes in descending order
# 7. res[i] *= postfix: Each element in res is multiplied by postfix, which represents the product of all elements to the right of i.
# 8. postfix *= nums[i]: The postfix variable is updated by multiplying it with nums[i], so it holds the product of all elements from the end of the list up to the next index.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
