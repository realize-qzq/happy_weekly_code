class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #BFS层次遍历，每层的最后一个
        if root is None:
            return []
        curlevel=[root]
        nextlevel=[]
        result=[]
        while curlevel:
            right_val=curlevel[-1].val
            result+=[right_val]
            for node in curlevel:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            curlevel=nextlevel
            nextlevel=[]
        return result