import java.util.*;

class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        int n = arrival.length;
        int[] count = new int[k];
        
        // Min-heap to store active servers: stores int[] {endTime, serverId}
        PriorityQueue<int[]> busyServers = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        
        // TreeSet to maintain all currently available servers in sorted order
        TreeSet<Integer> availableServers = new TreeSet<>();
        for (int i = 0; i < k; i++) {
            availableServers.add(i);
        }
        
        for (int i = 0; i < n; i++) {
            int startTime = arrival[i];
            int endTime = startTime + load[i];
            
            // Free up servers whose tasks have finished by the current request's arrival time
            while (!busyServers.isEmpty() && busyServers.peek()[0] <= startTime) {
                availableServers.add(busyServers.poll()[1]);
            }
            
            // If no servers are available, drop this request
            if (availableServers.isEmpty()) {
                continue;
            }
            
            // Find the first available server >= (i % k)
            Integer serverId = availableServers.ceiling(i % k);
            
            // If none exist >= (i % k), wrap around and take the smallest available server ID from the beginning (0)
            if (serverId == null) {
                serverId = availableServers.first();
            }
            
            // Assign the request to this server
            availableServers.remove(serverId);
            busyServers.offer(new int[]{endTime, serverId});
            count[serverId]++;
        }
        
        // Find the maximum number of requests handled by any server
        int maxRequests = 0;
        for (int c : count) {
            maxRequests = Math.max(maxRequests, c);
        }
        
        // Collect all servers that handled the maximum number of requests
        List<Integer> busiest = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (count[i] == maxRequests) {
                busiest.add(i);
            }
        }
        
        return busiest;
    }
}