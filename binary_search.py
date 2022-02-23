arr = [i for i in range(1, 1000000)]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        elif target < arr[mid]:
            right = mid - 1
            print(right)
            
        else:
            left = mid + 1
            print(left)
        
    return -1
            

print(binary_search(arr, 1))
