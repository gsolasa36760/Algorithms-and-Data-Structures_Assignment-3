"""Implementing a hash table involves using chaining for collision resolution and a universal hash function to distribute keys efficiently across the table.
Inserting key-value pairs involves calculating the index and adding them to the corresponding bucket. Searching retrieves values by finding the associated
key, and deleting removes key-value pairs from the table. Displaying the table shows the contents of each bucket, listing the keys and their associated values.
"""

class HashTable:
    def __init__(self, size):
        # Initializing the hash table with a given size
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calculating the hash value using a universal hash function
        prime = 31
        hash_value = 0
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % self.size
        return hash_value

    def insert(self, key, value):
        # Inserting a key-value pair into the hash table
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Adding the key-value pair to the bucket if the key doesn't exist
        self.table[index].append((key, value))

    def search(self, key):
        # Searching for a value associated with the key
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        # Deleting a key-value pair from the hash table
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        # Displaying the contents of the hash table
        for i, bucket in enumerate(self.table):
            if bucket:  # Checking if the bucket is not empty
                print(f"Index {i}: {bucket}")

# Example usage of the hash table

# Creating a hash table with size 10
ht = HashTable(10)

# Inserting key-value pairs
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)
ht.insert("grape", 4)

# Searching for a key
print(f"Search for 'banana': {ht.search('banana')}")

# Deleting a key-value pair
ht.delete("orange")

# Searching for a deleted key
print(f"Search for 'orange': {ht.search('orange')}")

# Displaying the hash table
ht.display()
