class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        cn = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                cn += 1
            else:
                cn = 1

            if cn > len(nums) // 2:
                return nums[i]

        return nums[0]