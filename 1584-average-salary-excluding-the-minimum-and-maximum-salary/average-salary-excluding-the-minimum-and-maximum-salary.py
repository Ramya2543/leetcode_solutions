class Solution:
    def average(self, salary: list[int]) -> float:
        least=min(salary)
        high=max(salary)
        salary.remove(least)
        salary.remove(high)
        sum=0
        for cur in salary:
            sum+=cur
        a=len(salary)
        return sum/a

        