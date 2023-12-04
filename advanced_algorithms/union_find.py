class UnionFind:
    def __init__(self, n):
        """
        Initializes a Union-Find data structure with 'n' elements.

        Parameters:
        - n (int): The number of elements in the Union-Find data structure.
        """
        # Initialize parent and rank dictionaries for each element from 1 to n
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            # Each element is initially its own parent, and the rank is set to 0
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n):
        """
        Finds the representative (root) of the set to which element 'n' belongs.

        Parameters:
        - n (int): The element for which to find the representative.

        Returns:
        - int: The representative of the set containing element 'n'.
        """
        # Find the root (representative) of the set to which n belongs
        p = self.parent[n]
        while p != self.parent[p]:
            # Path compression: Make every other node in the path point to its grandparent
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        """
        Unions the sets to which elements 'n1' and 'n2' belong.

        Parameters:
        - n1 (int): The first element.
        - n2 (int): The second element.

        Returns:
        - bool: True if the union is successful, False if the elements are already in the same set.
        """
        # Find the roots of the sets to which n1 and n2 belong
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            # If both elements are already in the same set, no need to union them
            return False

        if self.rank[p1] > self.rank[p2]:
            # Union by rank: Attach the shorter tree to the root of the taller tree
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            # If ranks are equal, choose one as the root and increment its rank
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True


# Example use cases
# Create a UnionFind object for a set of 5 elements
uf = UnionFind(5)

# Perform union operations
uf.union(1, 2)
uf.union(2, 3)

# Find representatives of elements
print(uf.find(1))  # Output: 1 (representative of the set containing 1, 2, and 3)
print(uf.find(4))  # Output: 4 (representative of the set containing only 4)
