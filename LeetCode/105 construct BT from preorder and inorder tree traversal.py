# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BASIC APPROACH IT IS RECURSIVE 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        r_v=preorder[0]
        root=TreeNode(r_v)
        mid=inorder.index(r_v)
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root

# optimized one
class Solution:
    def buildTree(self, preorder, inorder):
        index_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
