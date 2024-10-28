# Valid Palindrome
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Logic: 
# 1. Go through each char, if alphabet or digit, add that char to the result. 
# 2. Return when read from both the sides it should be same(Palindrome)

def isPalindrome(s):
  new = ''
  for i in s:
      if i.isalpha() or i.isdigit():
          new += i.lower()
  return (new==new[::-1])
