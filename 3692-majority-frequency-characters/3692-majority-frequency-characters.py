class Solution:
    def majorityFrequencyGroup(self, s: str) -> str: 
        count = {}

        for ch in s:
            if ch in count:
                continue
            else:
                count[ch] = s.count(ch)

        groups = {}

        for ch, freq in count.items():
            if freq not in groups:
                groups[freq] = []
            groups[freq].append(ch)

        max_size = 0
        max_freq = 0
        answer = ""

        for freq, chars in groups.items():
            if len(chars) > max_size or (len(chars) == max_size and freq > max_freq):
                max_size = len(chars)
                max_freq = freq
                answer = ''.join(chars)

        return answer
            
        

        
