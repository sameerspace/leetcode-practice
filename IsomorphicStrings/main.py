class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            if s[i] not in list(map.keys()) and t[i] not in list(map.values()):
                map[s[i]] = t[i]

            elif map.get(s[i]) != t[i]:
                return False

        return True
