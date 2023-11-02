def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            j += 1
            nums[j] = nums[i]

    return j + 1
