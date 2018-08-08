"""
Author: Ayoub Omari
Date: 08/08/2018
Problem: Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.
We need to return the least number of intervals the CPU will take to finish all the given tasks.
"""

def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    if len(tasks)==0 or len(tasks)==1: return len(tasks)
    counts = {}
    maxCount = 0
    nbMaxCount = 0
    for task in tasks:
        counts[task] = counts.setdefault(task, 0)+1
        if counts[task] == maxCount:
            nbMaxCount += 1
        elif counts[task] > maxCount:
            maxCount = counts[task]
            nbMaxCount = 1

    return max(len(tasks), maxCount + (maxCount-1)*n + nbMaxCount-1)
