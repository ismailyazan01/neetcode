class Pair:
    def __init__(self, key, val):
        """
        A simple key-value pair class.

        Parameters:
        - key: The key of the pair.
        - val: The value associated with the key.
        """
        self.key = key
        self.val = val


class HashMap:
    def __init__(self):
        """
        Implementation of a basic hash map using open addressing for collision resolution.

        Attributes:
        - size: The number of key-value pairs in the map.
        - capacity: The capacity of the underlying array.
        - map: The array to store key-value pairs.
        """
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        """
        Hashes the given key to determine the index in the map.

        Parameters:
        - key: The key to be hashed.

        Returns:
        - The index in the map.
        """
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        """
        Get the value associated with the given key.

        Parameters:
        - key: The key for which to retrieve the value.

        Returns:
        - The value associated with the key, or None if the key is not in the map.
        """
        index = self.hash(key)

        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        """
        Insert or update a key-value pair in the map.

        Parameters:
        - key: The key to be inserted or updated.
        - val: The value to be associated with the key.
        """
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity

    def remove(self, key):
        """
        Remove the key-value pair with the given key from the map.

        Parameters:
        - key: The key to be removed.
        """
        if not self.get(key):
            return

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        """
        Resize and rehash the map when the size exceeds half of the capacity.
        """
        self.capacity = 2 * self.capacity
        new_map = [None] * self.capacity

        old_map = self.map
        self.map = new_map
        self.size = 0
        for pair in old_map:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        """
        Print the key-value pairs in the map.
        """
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)


# Example Usage:

# Create a hash map
hash_map = HashMap()

# Put key-value pairs into the map
hash_map.put("apple", 5)
hash_map.put("banana", 3)
hash_map.put("orange", 8)

print("Original Hash Map:")
hash_map.print()

# Get value for a key
value_for_banana = hash_map.get("banana")
print(f"Value for 'banana': {value_for_banana}")

# Remove a key-value pair
hash_map.remove("apple")

print("Hash Map after removing 'apple':")
hash_map.print()
