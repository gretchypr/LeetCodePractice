def doesValidArrayExist(derived):
    """
    :type derived: List[int]
    :rtype: bool
    """
    n = len(derived)
    original = [False]*n
    for i in range(n-1):
        if derived[i] == 1:
            original[(i + 1) % n] = not original[i]
        else:
            original[(i + 1) % n] = original[i]

        if i > 0 and original[i - 1] ^ original[i] != derived[i-1]:
            return False

    # results = [original[i] ^ original[(i + 1)%n] for i in range(n)]

    # return derived == results
    return original[n - 1] ^ original[0] == derived[n - 1]