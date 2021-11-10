import math
from random import randint


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def isPrime(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt = math.floor(math.sqrt(n))
    for i in range(3, sqrt+1, 2):
        if n % i == 0:
            return False
    return True


def Prime(n: int):
    primeFlag = False
    while not primeFlag:
        n += 1
        if isPrime(n):
            primeFlag = True
    return n


def Pow2(n: int):
    n = n-1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 16
    return n+1


class HashTable:
    def __init__(self, capacity: int, type: int):
        self.type = type
        if type == 0:
            # Division
            self.capacity = Prime(capacity)
        if type == 1:
            # Multiplication
            self.capacity = Pow2(capacity)
        if type == 2:
            # Universal
            self.capacity = capacity
            self.p = Prime(1500)  # Prime greater than largest possible key
            self.a = randint(1, self.p)
            self.b = randint(0, self.p)
            print("Chosen Universal Hash parameters (P,A,B)",
                  self.p, self.a, self.b)
        print("Chosen capacity", self.capacity)
        self.size = 0
        self.buckets = [None]*self.capacity

    def Hash(self, key):
        if self.type == 0:
            return key % self.capacity
        if self.type == 1:
            return (math.floor(0.618*key) % (self.capacity))
        if self.type == 2:
            return ((self.a*key+self.b) % self.p) % self.capacity

    def insert(self, key, value):
        hashed = self.Hash(key)
        self.size += 1
        node = self.buckets[hashed]
        if(node):
            while(node.next):
                node = node.next
            node.next = Node(key, value)
            return
        self.buckets[hashed] = Node(key, value)

    def search(self, key):
        hashed = self.Hash(key)
        node = self.buckets[hashed]
        if(node):
            while(node):
                if(node.key == key):
                    print(node.value)
                    return
                node = node.next
        print('Not found')

    def remove(self, key):
        hashed = self.Hash(key)
        node = self.buckets[hashed]
        prev = None
        if(node):
            while(node):
                if(node.key == key):
                    self.size -= 1
                    if(prev):
                        prev.next = node.next
                        print("Removed", node.value)
                        return
                    else:
                        print("Removed", node.value)
                        self.buckets[hashed] = node.next
                        return
                prev = node
                node = node.next
        print('Not found')


table = HashTable(16, 2)
table.insert(1000, 'A')
table.insert(12, 'B')
table.insert(1023, 'C')
table.insert(4, 'D')
table.insert(14, 'E')
table.insert(24, 'F')
table.insert(34, 'G')
print(table.size)
print(table.buckets)

# table.remove(4)
# table.remove(24)
# table.remove(34)

# print(table.size)
# print(table.buckets[4])
