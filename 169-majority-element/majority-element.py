class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = set (nums)
        mx_count = 0
        mx_element = 0

        for i in element:
            cnt = nums.count(i)
            if mx_count <= cnt:
                mx_count = cnt
                mx_element = i
            
            if mx_count > len(nums)/2:
                break
        
        return mx_element


        