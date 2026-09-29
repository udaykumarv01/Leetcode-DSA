class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            remainder = n%2
            binary = str(remainder) + binary
            n = n//2
        binary = binary[::-1]
        return int(binary, 2)