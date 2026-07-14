from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)


        i = 0

        while i < n:
            value = nums[i]
            correct_index = value - 1

            if (
                1 <= value <= n
                and nums[correct_index] != value
            ):
                nums[i], nums[correct_index] = (
                    nums[correct_index],
                    nums[i],
                )
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1