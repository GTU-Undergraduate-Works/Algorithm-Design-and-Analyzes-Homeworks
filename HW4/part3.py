def k_sort(sorted_arrays):
    n = len(sorted_arrays)
    if n < 1:
        return []
    if n == 1:
        return sorted_arrays[0]

    middle = n // 2
    return merge(k_sort(sorted_arrays[:middle]), k_sort(sorted_arrays[middle:]))



def merge(arr1, arr2):


    n1 = len(arr1)
    n2 = len(arr2)
    merged_arr = [0]*(n1+n2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged_arr[k] = arr1[i]
            i += 1
        else:
            merged_arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        merged_arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        merged_arr[k] = arr2[j]
        j += 1
        k += 1
    return merged_arr



arr1 = [0,2,4,6,8,10,12,14,16,18,20]
arr2 = [1,3,5,7,9,11,13,15,17,19,21]
arr3 = [22,23,24,25,26,27,28,29,30,31,32]
arr4 = [42,43,44,45,46,47,48,49,50,51,52]
arr5 = [30,33,35,37,39,41,43,45,47,49,51]


arr6 = [arr1, arr2, arr3, arr4, arr5]
print(k_sort(arr6))