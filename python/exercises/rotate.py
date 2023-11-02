def rotate(nums, k):
    if k % len(nums) == 0:
        return

    position = (len(nums) - k) % len(nums)
    temp = nums[:position]
    nums[:k] = nums[position:] + temp
    nums[k:] = temp
