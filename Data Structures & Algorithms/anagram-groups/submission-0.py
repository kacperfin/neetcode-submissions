class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            l = [0] * 26   

            for character in string:
                idx = ord(character) - ord('a')
                l[idx] += 1
            tpl = tuple(l)

            if tpl not in d:
                d[tpl] = [string]
            else:
                d[tpl].append(string)

        return [value for key, value in d.items()]