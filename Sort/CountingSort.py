from typing import List


def CountingSort(A: List[int]) -> List[int]:
    # Pythonic way
    k = 10  # can be computed if we are unaware of max
    n = len(A)
    L = [[] for _ in range(k+1)]
    for j in range(n):
        L[A[j]].append(A[j])
    output = []
    for i in range(k+1):
        output.extend(L[i])
    return output


arr = [4, 2, 2, 8, 3, 3, 1]
print(CountingSort(arr))
