class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) -1
        n = 0
       

        while (len(matrix[0]) > m >=0 ) and (len(matrix) > n >=0 ):
            
            if matrix[n][m] == target:
                return True
            elif matrix[n][m] > target:
                m-=1
            elif matrix[n][m] < target:
                n+=1
            else:
                return False
        
        return False



        