
class Hashtable():
    def __init__(self):
        self.table = [[], [], [], [], [], [], [], []]
        self.hashtable = 0

    def hash(self, value):
        hashkey = 0
        for i in value:
            hashkey += ord(i)
        hashkey = hashkey % 8
        return hashkey

    def get(self, key):
        for i in self.table[self.hash(key)]:
            if i[0] == key:
                return i[1]

    def get_size(self):
        count = 0
        for i in self.table:
            count += len(i)
        return count

    def add(self, key, value):
        self.table[self.hash(key)].append((key, value))
        self.hashtable += 1

    def remove(self, key):
        for i in self.table[self.hash(key)]:
            if i[0] == key:
                self.table[self.hash(key)].remove(i)
                self.hashtable -= 1

    def is_empty(self):
        for i in self.table:
            if len(i) > 0:
                return False
        return True
    
    def __len__(self):
        return self.hashtable

data = ["goat", "pig", "chicken", "dog", "lion", "tiger", "cow", "cat"]

# make a hash table with key-value pairs: "goat": 0, "pig": 1, "chicken": 2, etc. 
h = Hashtable()
for i in range(len(data)):
    h.add(data[i], i)       # the key is data[i], the value is i

# print the hash table items
for key in data:
    print(h.get(key))
 
# test the method get() and if items in the hash table are correct
for i in range(len(data)): 
    assert h.get(data[i]) == i 

# test the method get_size()
n = h.get_size() # it depends on the default value of your hash table
assert n == 8 
assert len(h) == 8 # it depends on the number of items in the hash table

# test the method remove() and is_empty()
for i in data: 
    h.remove(i) 
print(h.is_empty()) 
assert h.is_empty()
assert len(h) == 0
