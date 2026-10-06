class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = []
        for ch in set(arr):            
            count.append(arr.count(ch))  

        array = set(count)
        if len(array) == len(count):
            return True
        else:
            return False