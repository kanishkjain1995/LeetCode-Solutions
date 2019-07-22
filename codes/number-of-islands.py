class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, vis):
            stack = [(i,j)]
            vis[(i,j)] = 1
            while stack:
                p, q = stack.pop()
                grid[p][q] = '0'
                for x, y in [[p-1,q],[p+1,q],[p,q-1],[p,q+1]]:
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == '1' and (x,y) not in vis:
                        stack.append((x, y))
                        vis[(x,y)] = 1
        count = 0
        vis = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    dfs(grid, i, j, vis)
        return count
