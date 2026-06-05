class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        gf = 0  # child pointer
        si = 0  # cookie pointer

        while gf < len(g) and si < len(s):
            if g[gf] <= s[si]:
                gf += 1
            si += 1

        return gf