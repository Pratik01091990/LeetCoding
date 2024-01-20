class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        element_set = set(arr)
        count = []
        for i in element_set:
            cnt = arr.count(i)
            if cnt in count:
                return False
            else:
                count.append(cnt)

        return True
            