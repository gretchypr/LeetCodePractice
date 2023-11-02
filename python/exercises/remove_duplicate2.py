def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time 36 ms
    # Space 13.5MB
    # j = 0
    # k = 0
    # for i in range(1, len(nums)):
    #     if nums[k] != nums[i]:
    #         nums[j] = nums[k]
    #         if i - k == 1:
    #             j += 1
    #         else:
    #             nums[j+1] = nums[k]
    #             j += 2
    #         k = i
    # if nums[k] == nums[len(nums)-1]:
    #     nums[j] = nums[k]
    #     if (len(nums) - 1) - k == 0:
    #         j += 1
    #     else:
    #         nums[j + 1] = nums[k]
    #         j += 2
    #
    # return j

    # Time: 40 ms
    # Space: 13.3MB
    # j = 1
    # k = 0
    # for i in range(1, len(nums)):
    #     if nums[i-1] == nums[i]:
    #         k += 1
    #     else:
    #         k = 0
    #     if k < 2:
    #         nums[j] = nums[i]
    #         j += 1
    # return j

    # time: 36ms
    # Space 13.5 MB
    if len(nums) <= 2:
        return 2
    j = 2
    for i in range(2, len(nums)):
        if nums[j - 2] != nums[i]:
            nums[j] = nums[i]
            j += 1
    return j
