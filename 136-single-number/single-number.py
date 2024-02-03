class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                l += 2
                r += 2
            else:
                return nums[l]

        return nums[len(nums) -1]

        