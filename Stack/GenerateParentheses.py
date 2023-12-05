#Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
class Solution:
   
    
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtracking(openset, closedset):
            if openset == closedset == n:
                res.append("".join(stack))
                return

            if openset < n:
                stack.append("(")
                backtracking(openset + 1, closedset)
                stack.pop()

            if closedset < openset:
                stack.append(")")
                backtracking(openset, closedset + 1)
                stack.pop()

        backtracking(0,0)
        return res
            
