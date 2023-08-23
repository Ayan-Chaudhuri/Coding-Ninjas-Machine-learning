# Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum sum and return 
# the maximum sum. That is, we can switch from one array to another array only at common elements. If no intersection 
# element is present, we need to take sum of all elements from the array with greater sum.


def max_sum_path(arr1, arr2):
    sum1 = sum2 = total_sum = i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            total_sum += max(sum1, sum2) + arr1[i]
            sum1 = sum2 = 0
            i += 1
            j += 1
    
    # Add remaining elements from arrays, if any
    while i < len(arr1):
        sum1 += arr1[i]
        i += 1
    while j < len(arr2):
        sum2 += arr2[j]
        j += 1
    
    total_sum += max(sum1, sum2)
    return total_sum


n = int(input())
arr1 = list(map(int, input().strip().split()))
m = int(input())
arr2 = list(map(int, input().strip().split()))

result = max_sum_path(arr1, arr2)
print(result)

