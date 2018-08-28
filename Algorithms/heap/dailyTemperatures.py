"""
Author : Ayoub Omari
Date : 28/08/2018

Problem :
Given a list of daily temperatures, produce a list that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Solution Complexity:
  - Space = O(n)
  - Time:
      * heapifying -> O(n)
      * insertions in indices = binary search + insert -> O(log(n)) + O(n) for each element -> O(n^2)
      
"""

def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    length = len(temperatures)
    l = []
    for i in range(len(temperatures)):
        l.append((temperatures[i], -i))

    heapq._heapify_max(l)

    res = [0]*length
    indices = []

    while len(l) > 0:
        temp = heapq._heappop_max(l)
        index = -temp[1]
        toInsertIn = bisect.bisect_left(indices, index)
        if toInsertIn <= len(indices)-1:
            res[index] = indices[toInsertIn]-index

        indices.insert(toInsertIn, index)

    return res
