from collections import deque

class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        answer = []

        queue = deque([root])

        while queue:

            size = len(queue)

            current = []

            for _ in range(size):

                node = queue.popleft()

                current.append(node.val)

                for child in node.children:
                    queue.append(child)

            answer.append(current)

        return answer