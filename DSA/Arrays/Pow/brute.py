class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            n = -n
            negative = True
        else:
            negative = False

        ans = 1

        for _ in range(n):
            ans *= x

        if negative:
            return 1 / ans

        return ans
#smtg i came up with for now 
