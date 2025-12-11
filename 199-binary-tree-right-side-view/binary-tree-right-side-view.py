# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        q=deque([root])
        while q:
            
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if i == n - 1:
                    ans.append(node.val)

                # BFS: push both children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
           
        return ans
        # queue=deque([root])
        # node=queue.popleft()
        # path=deque([node])
        # ans=[]
        # while path:
        #     node=path.popleft()
        #     for j in root[node].right:
        #         ans.append(j)
        #         path.append(j)
        # return ans

                
