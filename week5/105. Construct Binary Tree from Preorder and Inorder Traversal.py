class Solution:
    def construct(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        root_val = preorder[0]
        root = TreeNode(root_val)
        ind = inorder.index(root_val)  # 长度，前面的长度都是左孩子的
        left_node = self.construct(preorder[1:1 + ind], inorder[:ind])
        root.left = left_node
        right_node = self.construct(preorder[1 + ind:], inorder[ind + 1:])
        root.right = right_node
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = self.construct(preorder, inorder)
        return root
