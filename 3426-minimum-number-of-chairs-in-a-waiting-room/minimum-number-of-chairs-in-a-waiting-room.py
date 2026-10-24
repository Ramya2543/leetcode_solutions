class Solution:
    def minimumChairs(self, s: str) -> int:
        people=0
        chairs=0
        for ch in s:
            if ch=='E':
                people+=1
            else:
                people-=1
            chairs=max(chairs,people)
        return chairs
        
        