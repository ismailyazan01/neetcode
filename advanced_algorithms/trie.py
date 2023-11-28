class TrieNode:
    def __init__(self):
        """
        Initializes a TrieNode object.

        Parameters:
        - None

        Returns:
        - None
        """
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        """
        Initializes a Trie object with a root TrieNode.

        Parameters:
        - None

        Returns:
        - None
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.

        Parameters:
        - word (str): The word to insert.

        Returns:
        - None
        """
        # Start from the root of the trie
        curr = self.root

        # Traverse through each character in the word
        for c in word:
            # If the character is not in the current node's children, add a new TrieNode
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Move to the next node in the trie
            curr = curr.children[c]

        # Mark the last node as the end of a word
        curr.word = True

    def search(self, word):
        """
        Searches for a word in the trie.

        Parameters:
        - word (str): The word to search for.

        Returns:
        - bool: True if the word is found, False otherwise.
        """
        # Start from the root of the trie
        curr = self.root

        # Traverse through each character in the word
        for c in word:
            # If the character is not in the current node's children, the word is not in the trie
            if c not in curr.children:
                return False
            # Move to the next node in the trie
            curr = curr.children[c]

        # Check if the last node is marked as the end of a word
        return curr.word

    def startsWith(self, prefix):
        """
        Checks if there is any word in the trie that starts with the given prefix.

        Parameters:
        - prefix (str): The prefix to check.

        Returns:
        - bool: True if there is any word with the given prefix, False otherwise.
        """
        # Start from the root of the trie
        curr = self.root

        # Traverse through each character in the prefix
        for c in prefix:
            # If the character is not in the current node's children, the prefix is not in the trie
            if c not in curr.children:
                return False
            # Move to the next node in the trie
            curr = curr.children[c]

        # The prefix is found in the trie
        return True


# Example Use Cases for Trie methods
trie = Trie()

# Use insert method
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

# Use search method
search_result_1 = trie.search("apple")
search_result_2 = trie.search("app")
search_result_3 = trie.search("orange")

# Use startsWith method
startsWith_result_1 = trie.startsWith("app")
startsWith_result_2 = trie.startsWith("ban")
startsWith_result_3 = trie.startsWith("ora")

# Displaying Results
print("Trie:")
print("Inserted words: 'apple', 'app', 'banana'")

print("\nSearch Results:")
print(f"Search 'apple': {search_result_1}")
print(f"Search 'app': {search_result_2}")
print(f"Search 'orange': {search_result_3}")

print("\nstartsWith Results:")
print(f"startsWith 'app': {startsWith_result_1}")
print(f"startsWith 'ban': {startsWith_result_2}")
print(f"startsWith 'ora': {startsWith_result_3}")
