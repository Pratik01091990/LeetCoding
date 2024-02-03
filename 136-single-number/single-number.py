class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #sprt the array so that the duplicates are together
        nums.sort()
        
        # Initite the window pair
        l = 0
        r = 1
        while r < len(nums):
            #check for each pair if not unique then shift the window
            if nums[l] == nums[r]:
                l += 2
                r += 2
            else:
                return nums[l]

        # if we dont find the unique the the last number is unique 
        return nums[len(nums) -1]

        