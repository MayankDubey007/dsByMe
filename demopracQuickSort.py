def partition(start, end, array):
    
    pivot_index = start
    pivot = array[pivot_index]
    
    while start < end:
    
        while start < len(array) and array[start] <= pivot:
            start += 1
    
        while array[end] > pivot:
            end -= 1
        if (start < end):
            array[start], array[end] = array[end], array[start]
    
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
def QuickSort(start, end, array):
    if(start < end):
        p = partition(start, end, array)
        QuickSort(array, p-1, array)
        QuickSort(p+1, end, array)



array = [1, 74, 3, 34, 12, 5]
print(QuickSort(0, len(array) - 1, array))
