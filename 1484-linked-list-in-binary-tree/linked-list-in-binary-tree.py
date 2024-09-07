class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        # Helper function to match the linked list from the current tree node
        def match(node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
            # If the linked list is fully matched, return True
            if not head:
                return True
            # If the tree node is None, or values don't match, return False
            if not node or node.val != head.val:
                return False
            
            # Recursively check left and right children with the next node in the linked list
            return match(node.left, head.next) or match(node.right, head.next)

        # Function to traverse the tree and look for matching starting points
        def traverse(mainnode: Optional[TreeNode]) -> bool:
            # If there's no more tree node, return False
            if not mainnode:
                return False
            # Check if the current tree node can be a starting point for the linked list
            if match(mainnode, head):
                return True
            # Otherwise, keep searching in the left and right subtrees
            return traverse(mainnode.left) or traverse(mainnode.right)
        
        # Start traversing from the root of the tree
        return traverse(root)
