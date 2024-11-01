def find_median(lst):
    def sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr 
    
    sort_list = sort(lst)

    n = len(sort_list)
    if n%2 == 1:
        median = sort_list[n//2]
    else:
        mid1 = sort_list[n//2 - 1]
        mid2 = sort_list[n//2]
        median = (mid1 + mid2)/2

    return median

numbers = [5, 2, 4, 3, 6]
print(find_median(numbers))