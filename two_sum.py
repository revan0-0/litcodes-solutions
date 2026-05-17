# LeetCode 1 - Two Sum
# Runtime: Beats 5.5%
# Status: Accepted - 63/63 test cases

class Solution:
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
