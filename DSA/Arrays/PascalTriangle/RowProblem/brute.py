
def solution(numRows):
    output= []
    output.append(1)
    multiplier = 1

    for i in range(numRows):
    
        multiplier *= (numRows - i)/(i+1)
        output.append(multiplier)
    
    output.append(1)
    return output

numRows = 5
pascalnumRows = solution(numRows)
print(pascalnumRows)

