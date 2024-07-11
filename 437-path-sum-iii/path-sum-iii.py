# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):

        # Initialize the result to store the number of valid paths
        self.result = 0

        # Initialize the cache with the base case: sum 0 has one occurrence
        cache = {0: 1}

        # Start the DFS traversal from the root with an initial path sum of 0
        self.dfs(root, target, 0, cache)

        # Return the total number of valid paths found
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # If the current node is None, return immediately (base case)
        if not root:
            return

        # Add the current node's value to the current path sum
        currPathSum += root.val

        # Calculate the old path sum needed to reach the target from the current path sum
        oldPathSum = currPathSum - target

        # Update the result with the number of valid paths ending at the current node
        self.result += cache.get(oldPathSum, 0)

        # Update the cache with the current path sum
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # Recursively call dfs on the left and right children of the current node
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        # Backtrack: remove the current path sum from the cache
        # This is necessary because we are moving back up the tree and the current path sum is no longer available
        cache[currPathSum] -= 1
    

        

        





#  brute force
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def __init__(self):
#         self.total_paths = 0
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

#         curr_sum = 0
#         def dfs(root,curr_sum):

#             if not root:
#                 return 
            

#             curr_sum +=root.val
#             if curr_sum ==  targetSum:
#                 self.total_paths +=1
            
#             dfs(root.left,curr_sum)
#             dfs(root.right,curr_sum)
        
#         def traverse(root):
#             if not root:
#                 return

#             dfs(root,0)
#             traverse(root.left)
#             traverse(root.right)
        

#         traverse(root)
#         return self.total_paths


        