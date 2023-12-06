# Examples :  

# Input: array = [1, 5, 4, 3]
# Output: 6
# Explanation : 
# 5 and 3 are distance 2 apart. 
# So the size of the base = 2. 
# Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6
class selfArray():
    def __init__(self):
        self.nums = []
    def Solution(self,nums):
        maxnums = 0
        a=0
        b=len(nums)-1
        while(a<b):
            if(nums[a]<nums[b]):
                maxnums = max(maxnums,nums[a]*(b-a))
                a+=1
            else:
                maxnums = max(maxnums,nums[b]*(b-a))
                b-=1
        return maxnums
        
if __name__ == '__main__':
    nums = [1, 5, 4, 3]
    two_sum_instance = selfArray()
    print(two_sum_instance.Solution(nums))
