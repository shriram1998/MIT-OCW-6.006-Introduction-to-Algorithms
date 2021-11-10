import math
import string

a = 128


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


corpus = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
translation_table = str.maketrans(string.ascii_uppercase,
                                  string.ascii_lowercase, " "+string.punctuation)
corpus = corpus.translate(translation_table)
search = "like"

prime = PrimeBelow(len(corpus))


class RollingHashADT:
    def __init__(self):
        self.size = 0
        self.hash = 0

    def append(self, char):
        # print('Append', char, ord(char))
        self.hash = (self.hash*a+ord(char)) % prime
        self.size += 1
        # print('Hash after append', self.hash)

    def skip(self, char):
        # print('Skip', char, ord(char))
        self.hash = (
            self.hash-(ord(char)*(a**(self.size-1)) % prime)) % prime
        self.size -= 1
        # print('Hash after skip', self.hash)

    def __call__(self):
        # print('Hash', self.hash)
        return self.hash


rc = RollingHashADT()
rs = RollingHashADT()

for i in range(len(search)):
    rc.append(corpus[i])
    rs.append(search[i])

for i in range(len(search), len(corpus)+1):
    # print('Iteration', i-len(search))
    # print('Corpus Hash', rc(), 'Search Hash', rs())
    if(rc() == rs()):
        print(corpus[i-len(search):i])
        if(search == corpus[i-len(search):i]):
            print('Search found at', i-len(search))
            break
    if(i == len(corpus)):
        print('Not found')
        break
    rc.skip(corpus[i-len(search)])
    rc.append(corpus[i])
