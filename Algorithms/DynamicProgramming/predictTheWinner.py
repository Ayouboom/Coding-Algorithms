"""
Author : Ayoub Omari
Date : 14/08/2018

Problem : 

Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on.
Each time a player picks a number, that number will not be available for the next player.
This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
You can assume each player plays to maximize his score.

Complexity analysis:
Time : O(n^2)
Space : O(n^2)
"""

def PredictTheWinner(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums)==0: return

    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][i] = nums[i]

    for j in range(len(nums)):
        for i in range(j-1, -1, -1):
            dp[i][j] = max(nums[j]-dp[i][j-1], nums[i]-dp[i+1][j])

    return dp[0][len(nums)-1] >= 0
