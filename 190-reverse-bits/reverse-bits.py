class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f'{n:032b}' 
        reversed_b = binary[::-1]
        return int(reversed_b,2)