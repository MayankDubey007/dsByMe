arr = [7,3,5,33,2,65,34]
n = len(arr)
for i in range(1,n):
    val = arr[i]  
    for j in range(i-1,-2,-1):           
        # if j < 0 : break
        if arr[j] > val:
            arr[j+1] = arr[j]
        else:                                
            break
    arr[j+1] = val
for num in arr:
    print(num,end=' ')
        