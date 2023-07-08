class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_(key)
        for i in self.table[index]:
            if i[0] == key:
                i[1] = value
                return
        self.table[index].append((key, value))

    def get_(self, key):
        index = self.hash_(key)
        for i in self.table[index]:
            if key == i[0]:
                print(i[1])

    def delete(self, key):
        index = self.hash_(key)
        for i in self.table[index]:
            if key == i[0]:
                del self.table[index]


c = HashTable(5)
c.insert("dayon", 22)
c.insert("roshan", 24)
c.insert("akhil", 22)
c.insert("irfan", 22)
c.insert("abin", 26)
print(c.table)
c.get_("abin")
c.delete("dayon")
print(c.table)
