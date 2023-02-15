class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        num_str = ""
        for digit in num:
            num_str += str(digit)

        number = int(num_str)
        ans = number + k
        output = []

        while ans != 0:
            output.append(ans % 10)
            ans = int(ans / 10)

        return output[::-1]


num = [1, 2, 6, 3, 0, 7, 1, 7, 1, 9, 7, 5, 6, 6, 4, 4, 0, 0, 6, 3]

sol = Solution()

print(sol.addToArrayForm(num, 516))
