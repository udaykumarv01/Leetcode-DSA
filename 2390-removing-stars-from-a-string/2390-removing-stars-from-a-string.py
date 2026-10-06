class Solution:
    def removeStars(self, s: str) -> str:
        idx = 0
        while idx < len(s):
            if s[idx] == '*':
                s = s[:idx-1] + s[idx+1:]
                idx -= 1
            else:
                idx += 1
        
        return s