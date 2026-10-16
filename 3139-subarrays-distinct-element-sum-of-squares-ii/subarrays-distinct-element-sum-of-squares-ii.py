class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)

    def push(self, node, l, r):
        if self.lazy[node] != 0:
            add = self.lazy[node]
            mid = (l + r) // 2
            
            # बाएँ बच्चे को अपडेट करें
            self.sum_val[2 * node] = (self.sum_val[2 * node] + 2 * add * self.tree[2 * node] + add * add * (mid - l + 1)) % 1000000007
            self.tree[2 * node] = (self.tree[2 * node] + add * (mid - l + 1)) % 1000000007
            self.lazy[2 * node] = (self.lazy[2 * node] + add) % 1000000007
            
            # दाएँ बच्चे को अपडेट करें
            self.sum_val[2 * node + 1] = (self.sum_val[2 * node + 1] + 2 * add * self.tree[2 * node + 1] + add * add * (r - mid)) % 1000000007
            self.tree[2 * node + 1] = (self.tree[2 * node + 1] + add * (r - mid)) % 1000000007
            self.lazy[2 * node + 1] = (self.lazy[2 * node + 1] + add) % 1000000007
            
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self.sum_val[node] = (self.sum_val[node] + 2 * val * self.tree[node] + val * val * (r - l + 1)) % 1000000007
            self.tree[node] = (self.tree[node] + val * (r - l + 1)) % 1000000007
            self.lazy[node] = (self.lazy[node] + val) % 1000000007
            return
        
        self.push(node, l, r)
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
            
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % 1000000007
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % 1000000007

    def query_sum(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.sum_val[node]
        
        self.push(node, l, r)
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res = (res + self.query_sum(2 * node, l, mid, ql, qr)) % 1000000007
        if qr > mid:
            res = (res + self.query_sum(2 * node + 1, mid + 1, r, ql, qr)) % 1000000007
        return res

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        st = SegmentTree(n)
        
        last_occurrence = {}
        total_sum = 0
        current_running_sum = 0
        
        for j in range(n):
            val = nums[j]
            prev_idx = last_occurrence.get(val, -1)
            last_occurrence[val] = j
            
            # रेंज [prev_idx + 1, j] को 1 से अपडेट करें
            st.update(1, 0, n - 1, prev_idx + 1, j, 1)
            
            # वर्तमान एंडिंग इंडेक्स तक के सभी सबअरे के स्क्वायर का सम प्राप्त करें
            current_running_sum = st.query_sum(1, 0, n - 1, 0, j)
            total_sum = (total_sum + current_running_sum) % MOD
            
        return total_sum