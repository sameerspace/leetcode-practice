class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        print(s)
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if stack[-1] != map[char]:
                    return False
                else:
                    stack.pop()

        if len(stack) == 0:
            return True
        return False



sol = Solution()
print(sol.isValid("[]{}"))
