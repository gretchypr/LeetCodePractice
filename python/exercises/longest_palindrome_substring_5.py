def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return 1 
    return recSearch(s, 0, n, 1)
def recSearch(s, low, high, currLength):
    if low >= high:
        return s[low if low >= 0 else high]
    half = (high + low) // 2
    if currLength >= (half - low) * 2 or currLength >= (high - half) * 2:
        return s[half]
    left = half - 1
    right = half + (0 if (high - low) % 2 == 0 else 1)
    result = s[half]
    while(left >= 0 and right <= len(s) and s[left] == s[right]):
        right += 1
        result = s[left:right]
        left -= 1
    currLength = len(result)
    L = recSearch(s, low, half, currLength)
    R = recSearch(s, half+1, high, currLength)
    if len(L) > len(R):
        return result if currLength > len(L) else L
    else:
        return result if currLength > len(R) else R
    

if __name__ == "__main__":
    # s = "babad"
    # s = "bcdefghhgfexyz"
    s = "efghhgfexyz"
    print(longestPalindrome(s))