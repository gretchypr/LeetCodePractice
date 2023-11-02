def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # Solution
    # time = 25 ms
    # space = 13.2 MB
    # i = 0
    # j = len(nums) - 1
    # c = 0
    # while i <= j:
    #     while j >= 0 and nums[j] == val:
    #         j -= 1
    #         nums.pop()
    #     while i < len(nums) and nums[i] != val:
    #         i += 1
    #     if i < j:
    #         temp = nums[i]
    #         nums[i] = nums[j]
    #         nums[j] = temp
    # return len(nums)
    # Other solution
    # time = 17 ms
    # space = 13.3 MB
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j
