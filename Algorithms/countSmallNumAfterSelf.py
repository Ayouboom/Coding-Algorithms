def countSmaller(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums)==0: return []
    processed = [nums[-1]]
    counts = [0]*len(nums)
    for i in range(len(nums)-2, -1, -1):
        start = bisect.bisect_left(processed, nums[i])
        processed.insert(start, nums[i])
        counts[i] = start
    return counts
