class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, item):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, item)]
        else:
            self.table[index].append((key, item))





