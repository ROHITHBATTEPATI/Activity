import random

def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1 

    for j in range(low, high):
        if arr[j] < pivot: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

   
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 

def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  
        quicksort_inplace(arr, low, pi - 1) 
        quicksort_inplace(arr, pi + 1, high)  

random_array = [random.uniform(0, 1) for _ in range(10)]
print("Unsorted Array:", random_array)
quicksort_inplace(random_array, 0, len(random_array) - 1)
print("Sorted Array using In-Place QuickSort:", random_array)
