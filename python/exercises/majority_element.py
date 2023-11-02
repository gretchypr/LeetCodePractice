def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time 141ms (24.58%)
    # Space 15.5MB (13.40 %)
    # nums.sort()
    # count = 1
    #
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i-1]:
    #         count += 1
    #     else:
    #         count = 1
    #     if count > (len(nums)/2):
    #         return nums[i]
    # return nums[0]

    # Time 140 ms (27.60%)
    # Space: 16.1MB (5.73%)
    # count = 0
    # value = nums[0]
    # for i in range(len(nums)):
    #     if count == 0:
    #         value = nums[i]
    #     if nums[i] == value:
    #         count += 1
    #     else:
    #         count -= 1
    # return value
    freq = {}
    for val in nums:
        if freq[val] != None:
            freq[val] = freq[val] + 1
        else:
            freq[val] = 1

    