"""
@Author : Ayoub Omari
@Date : 18/08/2018

Problem : You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S
"""

class TargetSum:
    
    def findTargetSumWays(self, nums, S):
    
        self.memo = [{} for _ in range(len(nums))]
        self.nums = nums
        return self.findTargetSumWays2(len(nums)-1, S)


    def findTargetSumWays2(self, end, S):
        if end==-1:
            return S==0
        
        if S in self.memo[end]:
            return self.memo[end][S]
        else:
            self.memo[end][S] = self.findTargetSumWays2(end-1, S-self.nums[end]) + self.findTargetSumWays2(end-1, S+self.nums[end])
            return self.memo[end][S]
