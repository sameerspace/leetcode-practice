class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = abs(x)
        nums = []
        while x != 0:
            nums.append(x % 10)
            x = int(x / 10)

        i = 0
        j = len(nums) - 1
        for x in range(0, int(len(nums) / 2)):
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1

        return True


sol = Solution()
print(sol.isPalindrome(2))
