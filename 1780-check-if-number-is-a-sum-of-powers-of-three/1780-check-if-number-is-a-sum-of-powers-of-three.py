class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 1

        while x <= n:
            x *= 3

        x //= 3

        while x > 0:
            if x <= n:
                n -= x
            x //= 3

        return n == 0