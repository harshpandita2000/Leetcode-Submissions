class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        current = s[0]
        change = 0
        for item in s:
            if item == current:
                continue
            else:
                current = item
                change+= 1
        return change
                
        