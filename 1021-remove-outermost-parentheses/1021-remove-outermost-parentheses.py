class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        for ch in s:
            if ch == '(' and opened >0:
                res.append(ch)
            if ch == ')' and opened > 1:
                res.append(ch)
            opened += 1if ch == '(' else -1
        return "".join(res)