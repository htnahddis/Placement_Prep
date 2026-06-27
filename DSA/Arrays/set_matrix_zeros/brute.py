class Solution:

    def change_row(self, matrix, row):
        for j in range(len(matrix[row])):
            if matrix[row][j] != 0:
                matrix[row][j] = "a"

    def change_col(self, matrix, col):
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = "a"

    def setZeroes(self, matrix):
        for i in range(len(matrix)): #m x n
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.change_row(matrix, i) #m
                    self.change_col(matrix, j) #n

        for i in range(len(matrix)):
            for j in range(len(matrix[0])): # m x n 
                if matrix[i][j] == "a":
                    matrix[i][j] = 0


#this si apprach is brute force converts all the numbers to -1 or smtg and then goes back to converting the markers to 0 thus giving set matrix zeroes 
