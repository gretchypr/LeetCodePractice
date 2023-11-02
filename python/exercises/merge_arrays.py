def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # My solution
    # Time: 28ms
    # Space: 13.3MB
    """a = m - 1
    b = n - 1
    i = (n + m) - 1
    while i >= 0 and a >= 0 and b >= 0:
        if nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1
        i -= 1

    while b >= 0:
        nums1[i] = nums2[b]
        b -= 1
        i -= 1
    while a >= 0:
        nums1[i] = nums1[a]
        a -= 1
        i -= 1"""

    # Other solution
    # Time: 24 ms
    # Space: 13.5 MB
    a = m - 1
    b = n - 1
    i = (n + m) - 1
    while b >= 0:
        if a >= 0 and nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        else:
            nums1[i] = nums2[b]
            b -= 1
        i -= 1