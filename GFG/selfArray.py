# Product of Array except itself
# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array 
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array 
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array 
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array 
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array 
# elements except 2 is 900

class selfArray():
    def __init__(self):
        self.nums = []
    def Solution(self,nums):
        res = [1] *len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
if __name__ == '__main__':
    nums = [10, 3, 5, 6, 2]
    two_sum_instance = selfArray()
    print(two_sum_instance.Solution(nums))
