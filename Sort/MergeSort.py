iter=0
def mergeSort(arr):
    global iter
    iter+=1
    print(iter*'\t','Level:',iter,' Array on entry: ',arr)
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print(iter*'\t','Level:',iter," Array Split up ",L,R)
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        print(iter*'\t','Level:',iter," D&D ",L,R)
        print(iter*'\t','Level:',iter,' Array before merge: ',arr)
        while i < len(L) and j < len(R):
            print(iter*'\t','Level:',iter," First Loop calc ",i,j,k,L[i],R[j])
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(iter*'\t','Level:',iter,' First loop i j k arr: ',i,j,k,arr)
        print(iter*'\t','Level:',iter," Atleast one part is sorted ",arr,'till ',k)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(iter*'\t','Level:',iter,' Adding remaining L ',i,k,arr)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(iter*'\t','Level:',iter,' Adding remaining R ',j,k,arr)
        print(iter*'\t','Level:',iter,"Both parts sorted ",arr)
    iter-=1
arr=[36,15,44,21,50]
mergeSort(arr)
print(arr)
