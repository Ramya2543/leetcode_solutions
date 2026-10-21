class Solution:
    def romanToInt(self, s: str) -> int:
        g={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        t=0
        for i in range(n):
            if  i<n-1 and g[s[i]]<g[s[i+1]]:
                t-=g[s[i]]
            else:
                t+=g[s[i]]
        return t

        