"""
Author : Ayoub Omari
Date : 11/08/2018

Problem : 
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Solution:
- Considering a house, we will decide to rob it if the global profit by robbing this house is greater than the global profit robbing
the previous one, the global profit is computed using the addition of the current house's profit and the global profit of the house
before the previous one.
"""

def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    profits = [0]*(len(nums)+2)

    for i in range(len(nums)):
        if nums[i]+profits[i]>profits[i+1]:
            profits[i+2]=nums[i]+profits[i]
        else:
            profits[i+2]=profits[i+1]

    return profits[-1]
