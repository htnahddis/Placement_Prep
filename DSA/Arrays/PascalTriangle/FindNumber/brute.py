
def solution(col,row):
  
    def factorial(col, end):
        for i in range(end-1):
            col *= col-1
            print("this is fucn: " , col)
        return col
    
    output = factorial(col, row)/factorial(row,row)


    return output
    

answer = solution(5,2)
print(answer)


#this method is to find the element in pascal's triangle using nCr method, optimised way

