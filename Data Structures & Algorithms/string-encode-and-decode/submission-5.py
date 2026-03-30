class Solution:

    def encode(self, strs: List[str]) -> str:
        len_strs = [str(len(string)) for string in strs]
        return f"{",".join(len_strs)}:{"".join(strs)}"

    def decode(self, s: str) -> List[str]:
        len_strs, message = s.split(":", 1)
        if not len_strs:
            return []
        len_strs = [int(l) for l in len_strs.split(",")]

        decoded = []
        pointer = 0
        for len_str in len_strs:
            decoded.append(message[pointer:pointer+len_str])
            pointer += len_str

        return decoded