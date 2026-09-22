class Node:
    def __init__(self, k):
        self.remain = [0] * k
        self.prod = 1

class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def merge(self, left_node, right_node):
        res = Node(self.k)
        res.prod = (left_node.prod * right_node.prod) % self.k
        for i in range(self.k):
            res.remain[i] = left_node.remain[i]
        for i in range(self.k):
            res.remain[(i * left_node.prod) % self.k] += right_node.remain[i]
        return res

    def build(self, nums, cur, left, right):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return
        mid = (left + right) // 2
        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)
        self.tree[cur] = self.merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

    def update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            for j in range(self.k):
                self.tree[tree_index].remain[j] = 0
            self.tree[tree_index].remain[val] = 1
            self.tree[tree_index].prod = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(2 * tree_index + 1, lo, mid, i, val)
        else:
            self.update(2 * tree_index + 2, mid + 1, hi, i, val)
        self.tree[tree_index] = self.merge(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def query(self, tree_index, lo, hi, i, j):
        if i <= lo and hi <= j:
            return self.tree[tree_index]
        if j < lo or hi < i:
            return Node(self.k)
        mid = (lo + hi) // 2
        left_res = self.query(2 * tree_index + 1, lo, mid, i, j)
        right_res = self.query(2 * tree_index + 2, mid + 1, hi, i, j)
        return self.merge(left_res, right_res)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        nums = [num % k for num in nums]
        for q in queries:
            q[1] %= k
            
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for index, value, start, x in queries:
            tree.update(0, 0, n - 1, index, value)
            subsegment = tree.query(0, 0, n - 1, start, n - 1)
            ans.append(subsegment.remain[x])
            
        return ans