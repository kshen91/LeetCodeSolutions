class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        ret = 0
        
        for index, h in enumerate(heights):
            if len(stack) == 0:
                stack.append(index)
                continue
                
            while len(stack) > 0 and h < heights[stack[-1]]:
                preIndex = stack.pop()
                if len(stack) != 0:
                    ret = max(ret, (index-stack[-1]-1)*heights[preIndex])
                else:
                    ret = max(ret, index * heights[preIndex])
            
            stack.append(index)
            
        while stack:
            i = stack.pop()
            if len(stack) != 0:
                ret = max(ret, (len(heights)-stack[-1]-1) * heights[i])
            else:
                ret = max(ret, len(heights) * heights[i])
            
        return ret                          
