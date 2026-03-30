class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for string in strs:
            d[frozenset(collections.Counter(string).items())].append(string)
        return list(d.values())