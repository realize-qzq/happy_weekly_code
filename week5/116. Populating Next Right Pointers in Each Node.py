class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        cur_level=[root]
        next_level=[]
        while cur_level:
            for ind,node in enumerate(cur_level):
                next_ind=ind+1
                if next_ind==len(cur_level):
                    node.next=None
                    #这里不能break，不然下面的next_level就到不了
                else:
                    node.next=cur_level[next_ind]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level=next_level
            next_level=[]
        return root