class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        for num in arr:
            freq[num]=1+freq.get(num,0)
        max_luck=-1
        for num in arr:
            if num==freq[num] and num>max_luck:
                max_luck=num
        return max_luck