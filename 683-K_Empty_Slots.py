class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        # Convert input to an array represents "flower in slot No. i will bloom on day No. days[i]"
        days = [0]*len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i+1
            
        # for k slots range, if all these k slots' bloom day is larger than it's left slot and right slot,
        # it will mean that on the larger day in days[left] and days[right], there exist k slots between them which are still
        # not blooming.
        # Also need to consider that if there exist multiple solutions and need to return the earliest day.
        
        possibleAns = []
        for left in range(len(days)-k-1):
            right = left+k+1
            if all(day > days[left] and day > days[right] for day in days[left+1:right]):
                possibleAns.append(max(days[left],days[right]))
        
        if len(possibleAns) > 0:
            return min(possibleAns)
        else:
            return -1
