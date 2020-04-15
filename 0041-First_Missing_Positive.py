class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, count = 0, 1
        length = len(nums)

        while i < length:
            num = nums[i]
            # only swaps numbers within range [1, len(nums))
            # skips swap if number already valid in index

            if 1 <= num < length and nums[num-1] != nums[i]:
                nums[num-1], nums[i] = nums[i], nums[num-1]
            else:
                i += 1

                # only iterates on next valid num
                # eg. swap [2, 1], now [1,2] needs iteration

                while count-1 < length and nums[count-1] == count:
                    count += 1
        return count
