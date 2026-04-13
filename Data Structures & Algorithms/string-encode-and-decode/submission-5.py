class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        r = ""
        for s in strs:
            r = r + str(len(s)) + '#' + s
        
        return r

    def decode(self, s: str) -> List[str]:
        r = []
        latest = 0
        while latest < len(s):
            t = False
            for i in range(latest, len(s)):
                if s[i].isnumeric():
                    temp_i = i
                    num = ""
                    while temp_i < len(s) and s[temp_i].isnumeric():
                        num += s[temp_i]
                        temp_i += 1
                    n = int(num)
                    if temp_i < len(s) and s[temp_i] == '#':
                        newS = ""
                        start_of_str = temp_i + 1
                        for x in range(start_of_str, start_of_str + n):
                            newS += s[x]
                        r.append(newS)
                        latest = start_of_str + n
                        t = True
                        break

            
            if not(t):
                return r
        return r