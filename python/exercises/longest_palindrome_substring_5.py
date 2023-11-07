def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return 1 
    return recSearch(s, 0, n)
def recSearch(s: str, low: int, high: int) -> str:
    if low == high:
        return ""
    half = (low + high) // 2
    left = half - 1
    right = half + 1
    result = result2 = s[half]
    while left >= 0 and right < len(s) and s[left] == s[right]:
        right += 1
        result = s[left:right]
        left -= 1
    left = half - 1
    right = half 
    while left >= 0 and right < len(s) and s[left] == s[right]:
        right += 1
        result2 = s[left:right]
        left -= 1
    result = result if len(result) > len(result2) else result2
    if len(result) > len(s) // 2:
        return result
    if (half + low) >= len(result):
        L = recSearch(s, low, half)
        result = result if len(result) > len(L) else L
    if (high - ((half + high) // 2)) * 2 >= len(result):
        R = recSearch(s, half + 1, high)
        result = result if len(result) > len(R) else R
    return result
            
    

if __name__ == "__main__":
    s1 = "babad"
    s2 = "bcdefghhgfexyz"
    s3 = "efghhgfexyz"
    s4 = "abcdefghijkyyz"
    s5 = "ahsy"
    print(longestPalindrome(s1))
    print(longestPalindrome(s2))
    print(longestPalindrome(s3))
    print(longestPalindrome(s4))
    print(longestPalindrome(s5))