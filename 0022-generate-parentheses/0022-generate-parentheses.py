class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        acc = set()

        def foo(open, close, s, ret):
            if open + close == n*2:
                ret.append(s)
                return
            if open < n:
                foo(open+1, close, s+"(", ret)
            if close < open:
                foo(open, close+1, s+")", ret)
        ret = []
        foo(0, 0, "", ret)
        return ret