def sort_by_frequency(arr):
   
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    

    sorted_arr = sorted(arr, key=lambda x: (-freq[x], -x))
    
    return sorted_arr

# Example usage:
arr = [2, 5, 6, 2, 3, 5, 5]
result = sort_by_frequency(arr)
print(result)
