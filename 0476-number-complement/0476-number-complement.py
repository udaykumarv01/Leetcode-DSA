class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        while num>0:
            remainder = num%2
            binary = str(remainder) + binary
            num = num//2
        
        com_num = ''.join( '1' if x == '0' else '0' for x in binary)

        return int(com_num, 2)