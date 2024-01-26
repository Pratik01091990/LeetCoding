class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        length = len(nums)
        while r < length:

            if nums[l] + nums[r] != target:
                r= r+1
                if r == length:
                    l = l+1
                    r = l+1

            else:
                return [l,r] 
                    
        return []