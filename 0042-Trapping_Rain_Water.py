class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height) < 3:
            return 0
        
        left = 0
        right = len(height) - 1
        
        maxLeft = 0
        maxRight = 0
        
        total = 0
        
        while left < right:
            if height[left] < height[right]:
                if maxLeft < height[left]:
                    maxLeft = height[left]
                else:
                    total += (maxLeft - height[left])
                
                left += 1
            
            else:
                if maxRight < height[right]:
                    maxRight = height[right]
                else:
                    total += (maxRight -  height[right])
                    
                right -= 1
        
        return total
