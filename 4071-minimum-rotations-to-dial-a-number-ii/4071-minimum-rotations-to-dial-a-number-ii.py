class Solution:
    def minRotations(self, n: int, s: str) -> int:
        n = len(s)
        value = 0
        results = []

        prefix = [0]
        for i in range(n):
            current = int(s[i])
            diff = abs(current - value)
            prefix.append(prefix[-1] + min(diff, 10 - diff))
            value = current

        results.append(prefix[n])

        suffix = [0] * (n + 1)
        for i in range(n - 2, -1, -1):
            diff = abs(int(s[i]) - int(s[i + 1]))
            suffix[i] = suffix[i + 1] + min(diff, 10 - diff)

        for k in range(n):
            value = int(s[k - 1]) if k > 0 else 0
            current = int(s[n - 1])
            diff = abs(current - value)
            results.append(prefix[k] + min(diff, 10 - diff) + suffix[k])

        return min(results)