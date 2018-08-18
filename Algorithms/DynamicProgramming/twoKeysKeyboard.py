"""
Author : Ayoub Omari
Date : 13/08/2018

Problem :
Initially on a notepad only one character 'A' is present.
We can perform two operations on this notepad for each step:

Copy All: We can copy all the characters present on the notepad (partial copy is not allowed).
Paste: We can paste the characters which are copied last time.
Given a number n. We have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
Output the minimum number of steps to get n 'A'.
"""

def minSteps(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n==1: return 0
    table = [0]*(n+1)
    table[1] = 0
    table[2] = 2

    for i in range(3, n//2+1):
        j = int(math.sqrt(i))
        mini = sys.maxsize
        while j >= 2:
            if i % j == 0:
                tmp = i//j
                if mini > min(table[j]+tmp, table[tmp]+j):
                    mini = min(table[j]+tmp, table[tmp]+j)

            j -= 1

        if mini == sys.maxsize:
            table[i] = i
        else:
            table[i] = mini

    j = int(math.sqrt(n))
    mini = sys.maxsize
    while j >= 2:
        if n % j == 0:
            tmp = n//j
            if mini > min(table[j]+tmp, table[tmp]+j):
                mini = min(table[j]+tmp, table[tmp]+j)

        j -= 1

    if mini == sys.maxsize:
        return n
    else:
        return mini
