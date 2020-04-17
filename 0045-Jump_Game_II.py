class Solution(object):
        
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        step = 0
        farestPointCanJumpBeforeNeedJump = 0
        needJumpPoint = 0

        for i in xrange(length):
            if i > needJumpPoint:
                needJumpPoint = farestPointCanJumpBeforeNeedJump
                step += 1

            if needJumpPoint >= length-1:
                return step

            farestPointCanJumpBeforeNeedJump = max(farestPointCanJumpBeforeNeedJump, i+nums[i])

        return step
