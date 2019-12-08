class Solution(object):
    def back(self,root):
        if root is None:
            return []
        l_candidate_sums = self.back(root.left)
        r_candidate_sums = self.back(root.right)
        if l_candidate_sums==[] and r_candidate_sums==[]:
            candidate_sums=[root.val]
        elif l_candidate_sums and r_candidate_sums==[]:
            candidate_sums=list(set([root.val+x for x in l_candidate_sums]))
        elif r_candidate_sums and l_candidate_sums==[]:
            candidate_sums=list(set([root.val+x for x in r_candidate_sums]))
        else:
            temp1 = set([root.val + x for x in l_candidate_sums])
            temp2 = set([root.val + x for x in r_candidate_sums])
            candidate_sums = list(temp1 | temp2)
        return candidate_sums

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #后序遍历，每个节点存了下面的所有cur_root->left的路劲和
        candidate_sums=self.back(root)
        return sum in candidate_sums
