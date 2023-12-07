#  Find Minimum in Rotated Sorted Array
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
def findMin(nums)
  res=nums[0]
  left_index=0
  right_index = len(nums)-1
  while(left_index<=right_index):
    if(nums[left_index]<nums[right_index]):
      res=min(res,nums[left_index])
      break;
    mid = (left_index+right_index)//2
    res=min(res,nums[mid])
    if(nums[mid]>=nums[left_index]):
      left_index=mid+1
    else:
      right_index=mid-1
  return(res)
if __name__==main():
  nums = []
  print(findMin(nums))
