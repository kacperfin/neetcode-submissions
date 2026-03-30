class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            l = [0] * 26  
            for character in string:
                l[ord(character) - ord('a')] += 1
            d[tuple(l)].append(string)
        return list(d.values())