class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
       
        total_area = sum(float(l) * l for x, y, l in squares)
        target_area = total_area / 2.0
        
        
        low = min(y for x, y, l in squares)
        high = max(y + l for x, y, l in squares)
        
        
        def get_area_below(Y):
            area = 0.0
            for x_i, y_i, l_i in squares:
                if Y <= y_i:
                    continue
                elif Y >= y_i + l_i:
                    area += float(l_i) * l_i
                else:
                    
                    height_below = Y - y_i
                    area += float(l_i) * height_below
            return area

        
        for _ in range(80):
            mid = (low + high) / 2
            if get_area_below(mid) < target_area:
                low = mid
            else:
                high = mid
                
        return round(high, 5)
