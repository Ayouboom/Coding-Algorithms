"""
Author : Ayoub Omari
Date : 11/08/2018

Problem: Given an integer array nums (positive and negative integers), find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Solution:
- DP version
"""

def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==0: return

    maxValue = nums[0]
    profits = [None]*len(nums)
    profits[0] = nums[0]

    for i in range(1,len(nums)):
        if profits[i-1]+nums[i] >= nums[i]:
            profits[i] = profits[i-1]+nums[i]
        else:
            profits[i] = nums[i]

        if maxValue < profits[i]:
            maxValue = profits[i]

    return maxValue
