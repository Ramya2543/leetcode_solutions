from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        arr=sorted(arr,reverse=True)
        counts=Counter(arr)
        for i,a in counts.items():
            if i==a:
                return i
        return -1
        