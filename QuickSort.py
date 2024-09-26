def quicksort(arr):
if len(arr) <= 1: return arr
else:
pivot = arr[len(arr) // 2]
left = [x for x in arr if x < pivot]
middle = [x for x in arr if x == pivot]
right = [x for x in arr if x > pivot]
return quicksort(left) + middle + quicksort(right)
# Example of Quicksort
arr = [random.uniform(0, 1) for _ in range(10)] print("Unsorted Array:", arr)
sorted_arr = quicksort(arr)
print("Sorted Array using QuickSort:", sorted_arr)
