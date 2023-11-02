def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # If the string is empty of only has 1 character then 
    # Just return its length
    if len(s) < 2:
        return len(s)
    # Left pointer
    i = 0
    # Current length of longest subtring
    length = 1
    # Set for storing all the characters of the current substring
    letters = set(s[i])
    # We run the right pointer
    for j in range(1, len(s)):
        # If we find a repeated letter we shift the left pointer
        
        if s[j] in letters:
            while s[i] != s[j]:
                letters.remove(s[i])
                i += 1
            i += 1
            
        letters.add(s[j])
        if len(letters) > length:
            length = len(letters)
    return length