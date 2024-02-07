class Solution:
    def frequencySort(self, s: str) -> str:
        freq=defaultdict(int)
        for word in s:
            freq[word]+= 1
        sorted_freq = sorted(freq.items(),key=itemgetter(1), reverse=True)
        sorted_letters = ""
        for letter, count in sorted_freq:
            sorted_letters += letter * count  
        return sorted_letters
            
        