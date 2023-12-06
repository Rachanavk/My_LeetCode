# Find duplicates
# Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.
class containsDuplicate():
    def __init__(self):
        self.nums = []
    def Solution(self,nums):
        hashMap = set()
        for i in nums:
            if i in hashMap:
                return True
            hashMap.add(i)
        return
            
if __name__ == '__main__':
    nums = [1, 2, 3, 6, 3, 6, 1]
    two_sum_instance = containsDuplicate()
    print(two_sum_instance.Solution(nums))
