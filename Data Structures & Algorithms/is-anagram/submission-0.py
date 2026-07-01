class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = s.strip()
        s2 = t.strip()

        if len(s1) != len(s2):
            return False

        return sorted(s1) == sorted(s2)