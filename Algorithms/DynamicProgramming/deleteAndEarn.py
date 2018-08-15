"""
Author : Ayoub Omari
Date : 15/08/2018

Problem:
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operation
"""

def deleteAndEarn1(self, nums):
    """
    Time Complexity:
      sort -> O(n logn) + 1 pass -> O(n) => O(nlogn)
      
    Space Complexity:
      profits => O(n)
      
    Note : We could use only two variables instead of the list profits as in each step we are only using profit[-1] and profits[-2]
    """
    nums.sort()
    profits = [0,0]
    i = 0
    previous = -2 # to have nums[0]>1+previous in the first test

    while i < len(nums):
        j = i + 1
        while j < len(nums) and nums[j]==nums[i]:
            j += 1
        counts = j - i
        if previous + 1 < nums[i]:
            profits.append(profits[-1]+nums[i]*counts)
        elif profits[-2]+nums[i]*counts > profits[-1]:
            profits.append(profits[-2]+nums[i]*counts)
        else:
            profits.append(profits[-1])

        previous = nums[i]
        i = j     
    return profits[-1]


def deleteAndEarn2(self, nums):
    """
    Time :
      O(n)*1pass + O(max(n))*2passes
    Space:
      O(max(n))
    """
    if not nums: return 0
    counts = {}
    mini = nums[0]
    maxi = nums[0]
    counts = {nums[0]: 1}
    #compute max, min, frequencies
    for i in range(1, len(nums)):
        if mini > nums[i]:
            mini = nums[i]
        elif maxi < nums[i]:
            maxi = nums[i]
        counts[nums[i]] = counts.setdefault(nums[i], 0)+1
    
    #add frequency to elements not in num
    for i in range(mini, maxi+1):
        if i not in counts:
            counts[i] = 0

    #apply dp solution
    last = 0
    current = 0
    previous = -2
    for i in range(mini, maxi + 1):
        if previous+1 < i:
            last = current
            current += i*counts[i]
        elif last+i*counts[i] > current:
            last, current = current, last+i*counts[i] 
        else:
            last = current
        previous = i

    return current
        
        
        
