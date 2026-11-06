import java.util.Arrays;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        int m = queries.length;
        // Store queries with their original indices: [query_time, original_index]
        int[][] sortedQueries = new int[m][2];
        for (int i = 0; i < m; i++) {
            sortedQueries[i][0] = queries[i];
            sortedQueries[i][1] = i;
        }

        // Sort queries by time
        Arrays.sort(sortedQueries, (a, b) -> Integer.compare(a[0], b[0]));

        // Sort logs by time
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));

        int[] ans = new int[m];
        int[] serverCount = new int[n + 1];
        int activeServers = 0;
        
        int logIdx = 0;
        int windowStart = 0;
        int windowEnd = 0;
        int numLogs = logs.length;

        for (int i = 0; i < m; i++) {
            int qTime = sortedQueries[i][0];
            int origIdx = sortedQueries[i][1];
            int leftBound = qTime - x;
            int rightBound = qTime;

            // Add logs that fall <= rightBound
            while (windowEnd < numLogs && logs[windowEnd][1] <= rightBound) {
                int serverId = logs[windowEnd][0];
                if (serverCount[serverId] == 0) {
                    activeServers++;
                }
                serverCount[serverId]++;
                windowEnd++;
            }

            // Remove logs that fall < leftBound
            while (windowStart < numLogs && logs[windowStart][1] < leftBound) {
                int serverId = logs[windowStart][0];
                serverCount[serverId]--;
                if (serverCount[serverId] == 0) {
                    activeServers--;
                }
                windowStart++;
            }

            // Zero-request servers = Total servers (n) - activeServers
            ans[origIdx] = n - activeServers;
        }

        return ans;
    }
}