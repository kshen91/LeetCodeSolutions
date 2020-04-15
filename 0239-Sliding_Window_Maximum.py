from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return []
        
        if len(nums) <= k:
            return [max(nums)]
        
        q = deque()
        ret = []
        
        for i, num in enumerate(nums):
            while len(q) != 0 and num > q[-1]:
                q.pop()
            
            q.append(nums[i])

            if i >= k-1:
                if nums[i-k] == q[0]:
                    q.popleft()
                ret.append(q[0])
        return ret
