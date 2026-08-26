class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            current_pos = nums[i]

            if 1 <= current_pos <= n and nums[i] != nums[current_pos - 1]:
                nums[i], nums[current_pos - 1] = nums[current_pos - 1], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        