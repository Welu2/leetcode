class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        res = [0] * n
        pref = 0
        for i, ch in enumerate(word):
            d = ord(ch) - ord('0')
            pref = (pref * 10 + d) % m
            if pref == 0:
                res[i] = 1
        return res