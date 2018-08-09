"""
Author: Ayoub Omari
Date: 09/08/2018
Problem : Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Solution: Binary search the first and the last position

"""

def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    start = 0
    end = len(nums)-1
    while start <= end:
        m = (start+end)//2
        if nums[m] >= target:
            end = m-1
        else:
            start = m+1

    if start >= len(nums) or nums[start]!=target:
        return [-1, -1]

    first = start

    start = first
    end = len(nums)-1
    while start <= end:
        m = (start+end)//2
        if nums[m] > target:
            end = m-1
        else:
            start = m+1
    if end < 0:
        return [first, first]


    return [first, end]
