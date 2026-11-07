import java.util.*;

class Solution {
    public int[] assignTasks(int[] servers, int[] tasks) {
        int n = servers.length;
        int m = tasks.length;
        int[] ans = new int[m];
        
        // freeServers stores: [weight, index]
        PriorityQueue<int[]> freeServers = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });
        
        for (int i = 0; i < n; i++) {
            freeServers.offer(new int[] { servers[i], i });
        }
        
        // busyServers stores: [freeTime, weight, index] using long to prevent overflow
        PriorityQueue<long[]> busyServers = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Long.compare(a[0], b[0]);
            if (a[1] != b[1]) return Long.compare(a[1], b[1]);
            return Long.compare(a[2], b[2]);
        });
        
        long currentTime = 0;
        for (int j = 0; j < m; j++) {
            currentTime = Math.max(currentTime, j);
            
            // Free up servers whose tasks are completed by currentTime
            while (!busyServers.isEmpty() && busyServers.peek()[0] <= currentTime) {
                long[] busy = busyServers.poll();
                freeServers.offer(new int[] { (int) busy[1], (int) busy[2] });
            }
            
            // If no servers are free, jump time to the next available server's finish time
            if (freeServers.isEmpty()) {
                currentTime = busyServers.peek()[0];
                while (!busyServers.isEmpty() && busyServers.peek()[0] <= currentTime) {
                    long[] busy = busyServers.poll();
                    freeServers.offer(new int[] { (int) busy[1], (int) busy[2] });
                }
            }
            
            // Assign the task to the best available free server
            int[] server = freeServers.poll();
            int weight = server[0];
            int index = server[1];
            
            ans[j] = index;
            busyServers.offer(new long[] { currentTime + tasks[j], weight, index });
        }
        
        return ans;
    }
}