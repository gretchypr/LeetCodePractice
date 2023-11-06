def findMedianSortedArrays(nums1, nums2):
    # Optimal solution found

    # Original solution
    # 86 ms Beats 77.55%
    # 16.62 MB beats 16.43%

    # Get sizes of both lists
    m = len(nums1)
    n = len(nums2)
    # Find midway of list if they were merged
    half = int((m + n) / 2)
    # Initial positions for both lists
    i = 0 
    j = 0
    # Midpoint value
    mid1 = 0
    # Previous midpoint value
    mid2 = 0
    # Iterate until half way through the "merged list"
    while (i + j) < (half+1):
        # Update to current value since it will be updated
        mid2 = mid1
        # If both indexed valid
        if i < m and j < n:
            # Update mid pint value based on who is smallest
            if nums1[i] < nums2[j]:
                mid1 = nums1[i]
                i += 1
            else:
                mid1 = nums2[j]
                j += 1
        elif i < m:
            mid1 = nums1[i]
            i += 1
        else:
            mid1 = nums2[j]
            j += 1
    if (m + n) % 2 == 0:
        return (mid1 + mid2)/2
    return mid1

# Optimal solution found:
# if len(nums1) > len(nums2):
#     nums1, nums2 = nums2, nums1
    
#     m, n = len(nums1), len(nums2)
#     low, high = 0, m
    
#     while low <= high:
#         partitionX = (low + high) // 2
#         partitionY = (m + n + 1) // 2 - partitionX
        
#         maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
#         maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
#         minX = float('inf') if partitionX == m else nums1[partitionX]
#         minY = float('inf') if partitionY == n else nums2[partitionY]
        
#         if maxX <= minY and maxY <= minX:
#             if (m + n) % 2 == 0:
#                 return (max(maxX, maxY) + min(minX, minY)) / 2
#             else:
#                 return max(maxX, maxY)
#         elif maxX > minY:
#             high = partitionX - 1
#         else:
#             low = partitionX + 1

if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6, 7, 8, 9, 10]
    print(findMedianSortedArrays(nums1, nums2))