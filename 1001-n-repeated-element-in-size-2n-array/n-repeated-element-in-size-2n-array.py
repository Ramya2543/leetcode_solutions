class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
       n=len(nums)//2
       counts=Counter(nums)
       for i,a in counts.items():
         if a==n:
            return i