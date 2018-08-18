"""
Author : Ayoub Omari
Date: 18/08/2018

Problem :
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).
"""

def isMatch(self, s, p):

    dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    dp[0][0] = True

    for j in range(1, len(p)+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
        else:
            break # they will remain False anyway so don't need to continue

    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if s[i-1]==p[j-1] or p[j-1]=='?':
                dp[i][j] = dp[i-1][j-1] # delete these charaters from s and p and check whether the subpattern and the substring match 

            elif p[j-1]=='*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j] # 0 times OR many times

    return dp[len(s)][len(p)] # the cell that takes the whole string and the whole pattern into account.
