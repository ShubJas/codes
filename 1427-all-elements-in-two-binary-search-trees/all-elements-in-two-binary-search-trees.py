# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = []  # List to store elements of the first tree in sorted order
        arr2 = []  # List to store elements of the second tree in sorted order

        # Perform in-order traversal on the first tree and store the elements in arr1
        self.inorder_dfs(root1, arr1)
        # Perform in-order traversal on the second tree and store the elements in arr2
        self.inorder_dfs(root2, arr2)

        res = []  # List to store the merged elements

        # Merge the two sorted lists arr1 and arr2
        while len(arr1) > 0 and len(arr2) > 0:
            if arr1[0] >= arr2[0]:
                res.append(arr2.pop(0))  # Append the smaller element from arr2 to res
            else:
                res.append(arr1.pop(0))  # Append the smaller element from arr1 to res

        # If there are remaining elements in arr1, append them to res
        if len(arr1) > 0:
            res += arr1
        # If there are remaining elements in arr2, append them to res
        else:
            res += arr2

        return res  # Return the merged sorted list

    def inorder_dfs(self, root: TreeNode, arr: List[int]):
        if not root:
            return  # If the current node is None, return immediately
        
        # Recursively traverse the left subtree
        self.inorder_dfs(root.left, arr)
        # Append the current node's value to the list
        arr.append(root.val)
        # Recursively traverse the right subtree
        self.inorder_dfs(root.right, arr)



#         # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         ans = []

#         def DFS(node):
#             if not node:
#                 return

#             ans.append(node.val)

#             DFS(node.left)
#             DFS(node.right)

#         DFS(root1)
#         DFS(root2)

#         return sorted(ans)
        