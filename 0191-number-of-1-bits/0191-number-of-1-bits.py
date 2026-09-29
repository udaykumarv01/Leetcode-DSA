class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = ""
        while n>0:
            remainder = n%2
            binary = str(remainder) + binary
            n = n//2
        return binary.count("1")