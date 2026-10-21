class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        s={}
        paragraph=paragraph.lower()
        paragraph="".join([char if char.isalnum() else ' 'for char in paragraph])
        l=paragraph.split()
        for i in l:
            s[i]=l.count(i)
        for i in banned:
            if i in s:
                s.pop(i,None)

        return max(s,key=s.get)
        