class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < len(s) and l < r:
            isCompared = False

            if s[l] != s[r] and s[l].isalnum() and s[r].isalnum():
                return False

            if not(s[l].isalnum()) or not(s[r].isalnum()):
                if not(s[l].isalnum()):
                    l = l + 1
                else:
                    r = r - 1
            else:
                l = l + 1
                r = r - 1

        return True