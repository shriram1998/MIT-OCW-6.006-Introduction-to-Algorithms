from typing import List


class Heap:
    def max_heapify(self, arr: List[int], i) -> None:
        largest = i
        L = 2*i+1
        R = 2*i+2
        if(L < len(arr) and arr[L] > arr[largest]):
            largest = L
        if(R < len(arr) and arr[R] > arr[largest]):
            largest = R
        if(largest != i):
            temp = arr[i]
            arr[i] = arr[largest]
            arr[largest] = temp
            return self.max_heapify(arr, largest)

    def heapify(self, arr: List[int]) -> None:
        for i in range(len(arr)//2, 0, -1):
            self.max_heapify(arr, i-1)

    def sort(self, arr: List[int]) -> List[int]:
        sortedArr = []
        self.heapify(arr)
        for _ in range(len(arr)):
            last = len(arr)-1

            sortedArr.append(arr[0])
            arr[0] = arr[last]
            arr = arr[:last]

            self.heapify(arr)
        return sortedArr


heap = Heap()
arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]
print(heap.sort(arr))
