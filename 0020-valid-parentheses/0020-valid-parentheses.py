class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_open = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack or stack[-1] != matching_open[bracket]:
                    return False
                stack.pop()

        return not stack