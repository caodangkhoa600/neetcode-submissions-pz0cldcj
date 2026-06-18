class Solution:
    def isValid(self, s: str) -> bool:
        r = []
        i = 0
        while i < len(s):
            if len(r) == 0 and not(s[i] == '(' or s[i] == "[" or s[i] == '{'):
                return False
            while i < len(s) and (s[i] == '(' or s[i] == "[" or s[i] == '{'):
                r.append(s[i])
                i = i + 1

            while i < len(s) and not(s[i] == '(' or s[i] == "[" or s[i] == '{') and len(r) > 0:
                p = r.pop()
                if p == '(' and s[i] != ')':
                    return False
                if p == '[' and s[i] != ']':
                    return False
                if p == '{' and s[i] != '}':
                    return False
                i = i + 1
                
        if len(r) > 0:
            return False
        return True