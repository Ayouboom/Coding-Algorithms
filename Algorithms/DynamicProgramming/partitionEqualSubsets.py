"""
Author : Ayoub Omari
Date : 17/08/2018

Problem : Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

"""

def canPartition(self, nums):

    # if there is a solution then sum(nums) is necessarily even and sum(subset1)=sum(nums)/2
    s = sum(nums)
    if s % 2:
        return False
    s //= 2

    dp = [[False for _ in range(s+1)] for _ in range(len(nums)+1)]

    dp[0][0] = True

    for i in range(1, len(nums)+1):
        for j in range(1, s+1):
            if j - nums[i-1] >= 0:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

        if dp[i][s]:
            return True

    return dp[len(nums)][s]
