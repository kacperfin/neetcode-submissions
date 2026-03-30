class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join((f'{len(string)}:{string}' for string in strs))

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        j = 0
        while j < len(s):
            if s[j] == ':':
                length = int(s[i:j])
                word = s[j+1:j+1+length]
                decoded.append(word)
                i = j + 1 + length
                j = i - 1
            j += 1
        return decoded