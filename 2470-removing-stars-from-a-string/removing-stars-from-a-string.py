class Solution:
    def removeStars(self, s: str) -> str:
        l = []
        for i in range(len(s)):
            if s[i] != '*':
                l.append(s[i])
            elif s[i] == '*':
                l.pop()
        
        return "".join(l)