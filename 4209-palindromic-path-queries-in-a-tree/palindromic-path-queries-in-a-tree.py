class SegmentTree:
    def __init__(self, n, init_vals):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n - 1, init_vals)

    def build(self, node, l, r, init_vals):
        if l == r:
            self.tree[node] = init_vals[l]
            return
        mid = (l + r) // 2
        self.build(2 * node, l, mid, init_vals)
        self.build(2 * node + 1, mid + 1, r, init_vals)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query(2 * node, l, mid, ql, qr) ^ self.query(2 * node + 1, mid + 1, r, ql, qr)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n

        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            sz[u] = 1
            max_sub = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sub:
                        max_sub = sz[v]
                        heavy[u] = v

        dfs1(0, -1, 0)

        cur_pos = 0
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)

        def char_to_mask(c):
            return 1 << (ord(c) - ord('a'))

        init_vals = [0] * n
        for i in range(n):
            init_vals[pos[i]] = char_to_mask(s[i])

        seg = SegmentTree(n, init_vals)

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    res ^= seg.query(1, 0, n - 1, pos[head[u]], pos[u])
                    u = parent[head[u]]
                else:
                    res ^= seg.query(1, 0, n - 1, pos[head[v]], pos[v])
                    v = parent[head[v]]
            if depth[u] > depth[v]:
                res ^= seg.query(1, 0, n - 1, pos[v], pos[u])
            else:
                res ^= seg.query(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                seg.update(1, 0, n - 1, pos[u], char_to_mask(c))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                # Check if at most one bit is set in the mask
                if mask & (mask - 1) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans