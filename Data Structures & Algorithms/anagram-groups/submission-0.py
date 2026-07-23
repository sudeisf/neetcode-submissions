from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for w in strs:
            sorted_word = "".join(sorted(w))
            anagram_group[sorted_word].append(w)
        
        return list(anagram_group.values())