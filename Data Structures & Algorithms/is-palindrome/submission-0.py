class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.lower()
        while i < len(s):
            if not s[i].isalnum():
                s = s[:i] + s[i + 1:]
                # print(s)
            else: 
                i += 1
        a = len(s)     
        for j in range(int(len(s) / 2)):
            if s[j] != s[a - j - 1]:
                return False
    
        return True
        