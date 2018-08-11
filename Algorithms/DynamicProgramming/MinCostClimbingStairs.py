"""
Author: Ayoub Omari
Date: 11/08/2018

Problem :
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once we pay the cost, we can either climb one or two steps. We need to find minimum cost to reach the top of the floor,
and we can either start from the step with index 0, or the step with index 1

Solution:
- DP version
- we iterate over stairs in the reverse order
- For every stair i we compute the global cost starting from this stair if it would be choosed.
"""

def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    globalProfit = [None]*(len(cost)+2)
    
    globalProfit[-1], globalProfit[-2] = 0, 0
    for i in range(len(cost)-1, -1, -1):
        globalProfit[i] = cost[i]+min(globalProfit[i+1], globalProfit[i+2])
        
    return min(globalProfit[0], globalProfit[1])