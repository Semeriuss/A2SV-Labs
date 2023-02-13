import java.util.PriorityQueue;

class Solution {
    // O(N*M*log(N*M)) time, O(N*M) space (N*M is the number of nodes in the graph
    public int shortestPathBinaryMatrix(int[][] grid) {
        int ROW = grid.length, COL = grid[0].length;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        if (grid[0][0] == 0)
            pq.offer(new int[] { 1, 0, 0 });
        boolean[][] vis = new boolean[ROW][COL];
        vis[0][0] = true;
        int[][] path = new int[][] {
                { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 }, { 1, 1 }, { -1, -1 }, { 1, -1 }, { -1, 1 }
        };
        while (!pq.isEmpty()) {
            int[] curNode = pq.poll();
            int cost = curNode[0], r = curNode[1], c = curNode[2];
            if (r == ROW - 1 && c == COL - 1)
                return cost;
            for (int[] nex : path) {
                int nr = r + nex[0], nc = c + nex[1];
                if (0 <= nr && nr < ROW && 0 <= nc && nc < COL && !vis[nr][nc] && grid[nr][nc] == 0) {
                    pq.offer(new int[] { cost + 1, nr, nc });
                    vis[nr][nc] = true;
                }
            }
        }
        return -1;
    }
}