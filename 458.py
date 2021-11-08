class solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        TC = O(N)
        """
        
        if nums is None or len(nums)==0:
            return 0
        
        count = 0
        result = 0
        
        for i in nums:
            if i == 1:
                count += 1
            else:
                result = max(reult, count)
                count = 0
        return max(result, count)

      

        
