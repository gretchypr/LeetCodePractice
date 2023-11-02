def circularGameLosers(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[int]
    """
    friends = [i + 1 for i in range(n)]
    position = 0
    index = 0
    while friends[position] != 0:
        friends[position] = 0
        index += 1
        position = (position + (index * k)) % n

    losers = [x for x in friends if x != 0]

    return losers