from collections import deque


class TreeNode:
    def __init__(self, val=0):
        """
        Definition for a binary tree node.

        Parameters:
        - val: The value of the node.
        """
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        Definition for a binary tree.

        Attributes:
        - root: The root node of the binary tree.
        """
        self.root = None

    def search(self, root, target):
        """
        Search for a target value in the binary tree.

        Parameters:
        - root: The root node of the binary tree.
        - target: The value to search for.

        Returns:
        - bool: True if the target is found, False otherwise.
        """
        if not root:
            return False
        if target > root.val:
            return self.search(root.right, target)
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return True

    def insert(self, root, val):
        """
        Insert a value into the binary tree.

        Parameters:
        - root: The root node of the binary tree.
        - val: The value to insert.

        Returns:
        - TreeNode: The root node of the modified binary tree.
        """
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        return root

    def print_in_order(self, root):
        """
        Print the binary tree in in-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if root:
            # Traverse the left subtree
            self.print_in_order(root.left)
            # Print the current node's value
            print(root.val, end=" ")
            # Traverse the right subtree
            self.print_in_order(root.right)

    def minValueNode(self, root):
        """
        Find the node with the minimum value in the binary tree.

        Parameters:
        - root: The root node of the binary tree.

        Returns:
        - TreeNode: The node with the minimum value.
        """
        while root and root.left:
            root = root.left
        return root

    def remove(self, root, val):
        """
        Remove a value from the binary tree.

        Parameters:
        - root: The root node of the binary tree.
        - val: The value to remove.

        Returns:
        - TreeNode: The root node of the modified binary tree.
        """
        if not root:
            return None
        if val > root.val:
            root.right = self.remove(root.right, val)
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else:
            if not root.left or not root.right:
                return root.left or root.right
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)
        return root

    def inorder(self, root):
        """
        Print the binary tree in in-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        """
        Print the binary tree in pre-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        """
        Print the binary tree in post-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    def bfs(self, root):
        """
        Perform a breadth-first search on the binary tree.

        Parameters:
        - root: The root node of the binary tree.
        """
        queue = deque()

        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

    def canReachLeaf(self, root):
        """
        Check if a binary tree can reach a leaf node.

        Parameters:
        - root: The root node of the binary tree.

        Returns:
        - bool: True if the binary tree can reach a leaf, False otherwise.
        """
        if not root or root.val == 0:
            return False

        if not root.left and not root.right:
            return True
        if self.canReachLeaf(root.left):
            return True
        if self.canReachLeaf(root.right):
            return True
        return False


# Example usage:
tree = BinaryTree()
tree.root = TreeNode(4)
tree.insert(tree.root, 7)
tree.insert(tree.root, 9)
tree.insert(tree.root, 3)
tree.insert(tree.root, 1)

print("In-Order Traversal:")
tree.print_in_order(tree.root)

print("\nBreadth-First Search:")
tree.bfs(tree.root)

print("\nCan Reach Leaf Node: ", tree.canReachLeaf(tree.root))
