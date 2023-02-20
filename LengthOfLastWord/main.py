class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split("")
        ans = []
        for item in res:
            if item != "" or item != " ":
                ans.append(item)

        return len(ans[-1])
