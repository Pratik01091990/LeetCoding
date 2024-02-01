class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        
        numset = set()
        for r in range(len(nums)):

            if len(numset) > k:
                numset.remove(nums[l])
                l+=1

            if nums[r] not in numset:
                numset.add(nums[r])
            else:
                return True


        return False
