#TwoSum
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2
class TwoSum():
    def __init__(self):
        self.A=[]
    def Solution(self,A,target):
        prev_val = {}
        for idx,value in enumerate(A):
            diff = target - value
            if(diff in prev_val):
                return [prev_val[diff],idx]
            prev_val[value] = idx
        return None


if __name__ == '__main__':
    A = [0, -1, 2, -3, 1]
    target = -2
    two_sum_instance = TwoSum()
    print(two_sum_instance.Solution(A, target))
