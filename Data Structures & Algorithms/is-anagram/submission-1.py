class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        for s_char, t_char in zip(s_sorted, t_sorted):
            if s_char != t_char:
                return False
        return True