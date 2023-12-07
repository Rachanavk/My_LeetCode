# Search a 2D Matrix
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL=len(matrix),len(matrix[0])
        top,bottom = 0,ROW-1
        while(top<=bottom):
          row = (top+bottom)//2
          if target >matrix[row][-1]:
            top=row+1
          elif target < matrix[row][0]:
            bottom = row-1
          else:
            break
        
        if not top<=bottom:
          return False
        l=0
        r=COL-1
        while(l<=r):
          mid=(l+r)//2
          if(matrix[row][mid]==target):
            return True
          elif(target>matrix[row][mid]):
            l=mid+1
          else:
            r=mid-1



        
