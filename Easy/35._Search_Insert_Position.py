class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if (nums[i] == target) or (nums[i] > target):
                return i
            elif nums[-1] < target:
                return len(nums)
            else:
                pass
