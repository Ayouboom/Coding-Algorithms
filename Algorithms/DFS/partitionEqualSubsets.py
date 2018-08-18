"""
Author: Ayoub Omari
Date: 18/08/2018

Problem : Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
"""

class PartitionEqualSubsets:

    def canPartition(self, nums):
        self.memo = {}
        self.nums = nums
        self.length = len(nums)
        
        # if there is a solution then sum(nums) is necessarily even and sum(subset1)=sum(nums)/2
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        
        return self.dfs(0, s)
    
    def dfs(self, start, s):
        if s==0: return True
        if start >= self.length: return False # s!=0
        
        left = False
        if s>=self.nums[start]:
            if start+1 in self.memo and s-self.nums[start] in self.memo[start+1]:
                left = False
            else:
                left = self.dfs(start+1, s-self.nums[start])
            
        if left: return True
        
        right = False
        if start+1 in self.memo and s in self.memo[start+1]:
            right = False
        else:
            right = self.dfs(start+1, s)
            
        if right: return True

        res = left or right
        
        if res==False: #if it is True the program ends so don't need to memoize for True case
            if start not in self.memo:
                self.memo[start] = set([s])
            else:
                self.memo[start].add(s)
        
        return res
        