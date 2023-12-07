class Solution:
    def search(self, nums: List[int], target: int) -> int:
      left_index = 0
      right_index = len(nums) - 1
      mid_index = 0

      while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = nums[mid_index]

        if mid_number == target:
          return mid_index

        if mid_number < target: # this means number is in right hand side of the list
          left_index = mid_index + 1
        else: # number to find is on left hand side of the list
          right_index = mid_index - 1

      return -1
    
        
