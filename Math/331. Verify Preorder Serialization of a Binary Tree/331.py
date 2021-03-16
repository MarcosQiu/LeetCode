class Solution:
    '''
    331. Verify Preorder Serialization of a Binary Tree
    Recursion
    '''
    def isValidSerialization(self, preorder: str) -> bool:
        preorder_list = preorder.split(',')
        return self.helper(preorder_list)

    def helper(self, preorder):
        # termination conditions
        # 1. empty
        # 2. preorder is '#'
        # 3. preorder has a length of 1,
        #    but not '#'
        # 4. preorder has length greater
        #    than 1, but not start with '#' 
        if preorder == []:
            return False
        if len(preorder) == 1:
            if preorder[0] == '#':
                return True
            else:
                return False
        
        if preorder[0] == '#':
            return False

        # get the preorder of left subtree
        idx = 1
        empty_node_expected = 1
        empty_node_seen = 0
        while idx < len(preorder):
            if preorder[idx] == '#':
                empty_node_seen += 1
                if empty_node_seen == empty_node_expected:
                    break
            else:
                empty_node_expected += 1
            idx += 1

        # if the right substree preorder is
        # empty, just return False
        if idx == len(preorder):
            return False

        left_subtree_preorder = preorder[1: idx + 1]
        right_subtree_preorder = preorder[idx + 1:]
        return self.helper(left_subtree_preorder) and self.helper(right_subtree_preorder)