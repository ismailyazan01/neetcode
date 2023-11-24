from collections import deque


class TreeNode:
    def __init__(self, val=0):
        """
        Definition for a binary tree node.

        Parameters:
        - val: The value of the node.
        """
        self.val = val  # Initializing the value of the node in the constructor.
        self.left = None  # Initialize the left child pointer as None for a binary tree node.
        self.right = None  # Initialize the right child pointer as None for a binary tree node.


class BinaryTree:
    def __init__(self):
        """
        Definition for a binary tree.

        Attributes:
        - root: The root node of the binary tree.
        """
        self.root = None  # Initializing an empty binary tree.

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
            return False  # If the root is None, the target value cannot be found.
        if target > root.val:
            return self.search(root.right, target)  # Recursively search in the right subtree.
        elif target < root.val:
            return self.search(root.left, target)  # Recursively search in the left subtree.
        else:
            return True  # The target value is equal to the current node's value.

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
            return TreeNode(val)  # If the root is None, create a new node with the given value.
        if val > root.val:
            root.right = self.insert(root.right, val)  # Recursively insert in the right subtree.
        elif val < root.val:
            root.left = self.insert(root.left, val)  # Recursively insert in the left subtree.
        return root  # Return the modified root.

    def minValueNode(self, root):
        """
        Find the node with the minimum value in the binary tree.

        Parameters:
        - root: The root node of the binary tree.

        Returns:
        - TreeNode: The node with the minimum value.
        """
        while root and root.left:
            root = root.left  # Traverse to the leftmost node in the tree.
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
            return None  # If the root is None, no removal is needed.
        if val > root.val:
            root.right = self.remove(root.right, val)  # Recursively remove from the right subtree.
        elif val < root.val:
            root.left = self.remove(root.left, val)  # Recursively remove from the left subtree.
        else:
            if not root.left or not root.right:
                return root.left or root.right  # If the node has one child or none, replace it with that child.
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.remove(root.right, minNode.val)  # If the node has two children, replace it with the minimum value node from the right subtree.
        return root

    def inorder(self, root):
        """
        Print the binary tree in in-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        self.inorder(root.left)  # Recursively traverse the left subtree.
        print(root.val)  # Print the current node's value.
        self.inorder(root.right)  # Recursively traverse the right subtree.

    def preorder(self, root):
        """
        Print the binary tree in pre-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        print(root.val)  # Print the current node's value.
        self.preorder(root.left)  # Recursively traverse the left subtree.
        self.preorder(root.right)  # Recursively traverse the right subtree.

    def postorder(self, root):
        """
        Print the binary tree in post-order traversal.

        Parameters:
        - root: The root node of the binary tree.
        """
        if not root:
            return
        self.postorder(root.left)  # Recursively traverse the left subtree.
        self.postorder(root.right)  # Recursively traverse the right subtree.
        print(root.val)  # Print the current node's value.

    def bfs(self, root):
        """
        Perform a breadth-first search on the binary tree.

        Parameters:
        - root: The root node of the binary tree.
        """
        queue = deque()

        if root:
            queue.append(root)  # If the root is not None, enqueue it.

        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()  # Dequeue the front node.
                print(curr.val)  # Print the value of the current node.
                if curr.left:
                    queue.append(curr.left)  # Enqueue the left child if it exists.
                if curr.right:
                    queue.append(curr.right)  # Enqueue the right child if it exists.
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
            return False  # If the root is None or has a value of 0, it cannot reach a leaf node.

        if not root.left and not root.right:
            return True  # If the root is a leaf node, the tree can reach a leaf.
        if self.canReachLeaf(root.left):
            return True  # Recursively check if the left subtree can reach a leaf.
        if self.canReachLeaf(root.right):
            return True  # Recursively check if the right subtree can reach a leaf.
        return False  # If none of the above conditions are met, the tree cannot reach a leaf.


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
