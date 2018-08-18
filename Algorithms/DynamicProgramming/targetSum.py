"""
Author : Ayoub Omari
Date : 18/08/2018

Problem : You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
"""
def findTargetSumWays(self, nums, S):

    mysum = sum(nums)

    if S > sum(nums): # [0,1,2,1] and S=10000000
        return 0

    s = mysum+S
    if s % 2:
        return 0


    target = s // 2
    dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]

    dp[0][0] = 1  # [] and 0 -> 1 subset (that is the empty array)

    for i in range(1, len(nums)+1):
        for j in range(0, target+1):
            dp[i][j] = dp[i-1][j]   #number of subsets found so far
            if nums[i-1]<=j:
                dp[i][j] += dp[i-1][j-nums[i-1]] # + number of subsets containing this element and summing to my subtarget

    return dp[len(nums)][target]
