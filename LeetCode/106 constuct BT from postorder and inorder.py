class Solution:
    def buildTree(self, inorder, postorder):
        post_idx = len(postorder) - 1
        idx = {val: i for i, val in enumerate(inorder)}

        def helper(l, r):
            nonlocal post_idx

            if l > r:
                return None

            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)
            mid = idx[root_val]

            # IMPORTANT: build right first
            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)

            return root

        return helper(0, len(inorder) - 1)
