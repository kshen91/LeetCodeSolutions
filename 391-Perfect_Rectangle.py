class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        area = 0
        outerCorners = set([])
        
        for rec in rectangles:
            corners = [(rec[0],rec[1]), (rec[0],rec[3]), (rec[2],rec[1]), (rec[2],rec[3])]
            area += (rec[3]-rec[1]) * (rec[2]-rec[0])
            
            for corner in corners:
                if corner not in outerCorners:
                    outerCorners.add(corner)
                else:
                    outerCorners.remove(corner)
                    
        if len(outerCorners) != 4:
            return False
        
        bl = min(outerCorners)
        tr = max(outerCorners)
        if area != (tr[1] - bl[1]) * (tr[0] - bl[0]):
            return False
        
        return True
