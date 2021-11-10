import math
from random import randint


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
    if n % 2 == 0:
        n += 1
    while not primeFlag:
        if isPrime(n):
            primeFlag = True
        else:
            n += 2
    return n


def PrimeBelow(n: int):
    primeFlag = False
    if n % 2 == 0:
        n -= 1
    while not primeFlag:
        if isPrime(n):
            primeFlag = True
        else:
            n -= 2
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

    def Hash2(self, key):
        prime = PrimeBelow(self.capacity)
        return prime-(key % prime)

    def insert(self, key, value):
        hash1 = self.Hash(key)
        self.size += 1
        node = self.buckets[hash1]
        newHash = hash1
        if(node):
            i = 0
            hash2 = self.Hash2(key)
            while(node and node != 'isDeleted'):
                i += 1
                newHash = (hash1+i*hash2) % self.capacity
                node = self.buckets[newHash]
            self.buckets[newHash] = (key, value)
            return
        self.buckets[newHash] = (key, value)
        print(self.size)
        if(self.size == self.capacity-1):
            print('Table full, Doubling')
            self.double()

    def double(self):
        self.capacity = self.capacity*2
        buckets = self.buckets
        self.size = 0
        self.buckets = [None]*self.capacity
        for item in buckets:
            if item and item != 'isDeleted':
                k, v = item
                self.insert(k, v)
        print('Table doubled')

    def shrink(self):
        self.capacity = self.capacity//2
        buckets = self.buckets
        self.size = 0
        self.buckets = [None]*self.capacity
        for item in buckets:
            if item and item != 'isDeleted':
                k, v = item
                self.insert(k, v)
        print('Table shrinked')

    def search(self, key):
        hash1 = self.Hash(key)
        node = self.buckets[hash1]
        if(node):
            i = 0
            hash2 = self.Hash2(key)
            while(node):
                if node != 'isDeleted':
                    k, v = node
                    if(k == key):
                        print(v)
                        return
                i += 1
                newHash = (hash1+i*hash2) % self.capacity
                node = self.buckets[newHash]
        print('Not found')

    def remove(self, key):
        hash1 = self.Hash(key)
        node = self.buckets[hash1]
        if(node):
            i = 0
            hash2 = self.Hash2(key)
            newHash = hash1
            while(node):
                if node != 'isDeleted':
                    k, v = node
                    if(k == key):
                        self.buckets[newHash] = 'isDeleted'
                        self.size -= 1
                        if(self.size < self.capacity//4):
                            self.shrink()
                        return
                i += 1
                newHash = (hash1+i*hash2) % self.capacity
                node = self.buckets[newHash]
        print('Not found')


table = HashTable(10, 1)
table.insert(1000, 'A')
table.insert(12, 'B')
table.insert(1023, 'C')
table.insert(4, 'D')
table.insert(14, 'E')
table.insert(24, 'F')
table.insert(34, 'G')
table.insert(5, 'D')
table.insert(15, 'E')
table.insert(25, 'F')
print(table.size)
print(table.buckets)

print(table.size)
print(table.buckets)
table.search(36)

table.remove(4)
table.remove(14)
table.remove(24)
table.remove(34)
table.remove(5)
table.remove(15)
table.remove(25)
print(table.size)
print(table.buckets)
