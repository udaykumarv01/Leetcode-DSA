class Solution:
    def convertDateToBinary(self, date: str) -> str:
        nums = []
        date = date.split("-")
        for ch in date :
            binary = ""
            ch = int(ch)
            while ch > 0 :
                remainder = ch%2
                binary = str(remainder) + binary
                ch = ch//2
            nums.append(binary)
        return"-".join(nums)
