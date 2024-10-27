# Input - [100,4,200,1,3,2] Output - 4
# Logic 
# 1. Convert input to Set
# 2. Variable to store the longest sequence
# 3. Go through each element and check if value-1 is in set. If present then that's the start of new seq else not.
# 4. If start of sequence, then check how many value+1 are present in seq
# 5. Return the longest length 

def longestConsecutive(nums):
  numSet = set(nums)
  longest = 0
  for i in nums:
      if i-1 not in numSet:
          length = 0
          while(i+length) in numSet:
              length +=1
          longest = max(longest, length)
  return longest 
