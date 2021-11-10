from typing import List


def RadixSort(A: List[int]) -> List[int]:
    b = max(A)
    place = 1
    while b/place > 0:
        A = CountingSort(A, place)
        place *= 10
    return A


def CountingSort(A: List[int], place: int) -> List[int]:
    # Pythonic way
    k = 9  # can be computed if we are unaware of max
    n = len(A)
    L = [[] for _ in range(k+1)]
    for j in range(n):
        index = A[j]//place
        L[index % 10].append(A[j])
    output = []
    for i in range(k+1):
        output.extend(L[i])
    return output


arr = [121, 432, 564, 23, 1, 45, 788]
print(RadixSort(arr))
