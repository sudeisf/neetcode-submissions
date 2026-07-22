from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        c = Counter(s)
        l = Counter(t)

        if c == l:
            return True
        else:
            return False