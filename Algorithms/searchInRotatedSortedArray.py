"""
Author: Ayoub Omari
Date: 10/08/2018

Problem :
- Suppose an array sorted in ascending order is rotated at some pivot unknown beforehand.
- You are given a target value to search. If found in the array return its index, otherwise return -1.

Solution:
- Binary search this position, keeping in mind that, for a sub array, if the first element is greater than the last element then
this sub array contains the pivot.

Complexity analysis:
Time: O(log(n))
Space: O(1)
"""

def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums)-1


    while start <= end:
        m = (start+end)//2
        if nums[m]==target:
            return m
        elif m==0:
            start += 1
        else:
            if start == end-1:
                if nums[start]==target:
                    return start
                start += 1
            elif nums[start] <= nums[m-1]:
                if nums[start]<=target and nums[m-1]>=target:
                    end = m-1
                else:
                    start = m+1
            else:
                if nums[start]<=target or nums[m-1]>=target:
                    end = m-1
                else:
                    start = m+1

    if start < len(nums) and nums[start]==target:
        return start
    return -1
