from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # ग्राफ को एडजैन्सी लिस्ट (Adjacency List) के रूप में तैयार करना
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components_count = 0
        
        for i in range(n):
            if not visited[i]:
                # एक नए कॉम्पोनेंट के लिए BFS शुरू करना
                queue = [i]
                visited[i] = True
                
                component_nodes = []
                head = 0
                
                # वर्तमान कॉम्पोनेंट के सभी नोड्स को खोजना
                while head < len(queue):
                    curr = queue[head]
                    head += 1
                    component_nodes.append(curr)
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                # कॉम्पोनेंट में कुल वर्टिक्स (V) की संख्या
                v_count = len(component_nodes)
                is_complete = True
                
                # जांचना कि क्या हर नोड की डिग्री (V - 1) है
                for node in component_nodes:
                    if len(adj[node]) != v_count - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count