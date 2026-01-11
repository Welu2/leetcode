class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        def largestRectangleInHistogram(heights):
            stack = [] # Stores indices: (height, index)
            max_h_area = 0
            
            # Add a sentinel 0 to flush the stack at the end
            for i, h in enumerate(heights + [0]):
                start = i
                while stack and stack[-1][0] >= h:
                    height, index = stack.pop()
                    max_h_area = max(max_h_area, height * (i - index))
                    start = index
                stack.append((h, start))
                
            return max_h_area
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Update the heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find the largest rectangle in the current histogram row
            max_area = max(max_area, largestRectangleInHistogram(heights))
            
        return max_area

        