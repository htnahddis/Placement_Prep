class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for row in range(numRows):
            output = []
            multiplier = 1

            for i in range(row + 1):
                output.append(multiplier)
                multiplier = multiplier * (row - i) // (i + 1)

            answer.append(output)

        return answer