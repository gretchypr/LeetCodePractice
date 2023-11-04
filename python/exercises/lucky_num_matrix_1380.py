def luckyNumbers (matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    minimums = set([min(matrix[i]) for i in range(len(matrix))])
    # Empty set for all the maximum values in each column
    maximums = set()
    # Find the maximums of each column
    for j in range(len(matrix[0])):
        # Get value at position j in each row
        col = [row[j] for row in matrix]
        # Store the maximum
        maximums.add(max(col))
    # Whichever value is in both sets are the lucky numbers
    luckies = list(minimums.intersection(maximums))
    return luckies
    
    # Original solution
    # 86 ms Beat 86.32%
    # 13.65MB Betas 16.84%
    
    # Set with all the minimum values per row
    # minimums = set([min(matrix[i]) for i in range(len(matrix))])
    # # Empty set for all the maximum values in each column
    # maximums = set()
    # # Find the maximums of each column
    # for col in range(len(matrix[0])):
    #     max = matrix[0][col]
    #     for row in range(len(matrix)):
    #         max = max if max > matrix[row][col] else matrix[row][col]
    #     # Add the max of the current column
    #     maximums.add(max)
    # # Whichever value is in both sets are the lucky numbers
    # luckies = list(minimums.intersection(maximums))
    # return luckies

if __name__ == "__main__":
    mat = [[3,6],[7,1],[5,2],[4,8]]
    # mat = [[3,7,8],[9,11,13],[15,16,17]]
    # mat = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    # mat = [[7,8],[1,2]]
    print(luckyNumbers(mat))
    