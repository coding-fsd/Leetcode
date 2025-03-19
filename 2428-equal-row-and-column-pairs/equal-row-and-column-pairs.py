class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = defaultdict(int)
        
        for row in grid:
            row_counts[tuple(row)] += 1
        
        count = 0
        for col in zip(*grid):  
            count += row_counts[col]

        return count
