class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        length = len(nums)
        while(r < length):
            e_l = nums[l]
            e_r = nums[r]
            if ((e_l + e_r) == target):
                return [l,r]
            else:
                r+=1
                if(r == length):
                    l+=1
                    r = l+1
                    
        return []