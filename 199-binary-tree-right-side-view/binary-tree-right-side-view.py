from collections import deque

class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        answer = []

        queue = deque([root])

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                if i == size - 1:
                    answer.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return answer