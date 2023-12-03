# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
class Solution:
    def is_match(self, ch1, ch2):
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        return match_dict[ch1] == ch2

    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]":
                if len(stack) == 0:
                    return False
                if not self.is_match(ch, stack.pop()):
                    return False

        return len(stack) == 0
