class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = left_count = i = 0
        n = len(s)
        while i < n:
            if s[i] == "(":
                left_count += 1
                i += 1
            else:
                if left_count > 0:
                    left_count -= 1
                else:
                    insertions += 1

                if i < (n-1) and s[i+1] == ")":
                    i += 2
                else:
                    insertions += 1
                    i += 1
        insertions += left_count * 2
        return insertions