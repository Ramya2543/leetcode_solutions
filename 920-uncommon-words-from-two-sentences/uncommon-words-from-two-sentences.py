class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s=s1+" "+s2
        l1=s.split()
        b={}
        for i in l1:
            b[i]=l1.count(i)
        l=[]
        for a,i in b.items():
            if i==1:
                l.append(a)
        return l
                    