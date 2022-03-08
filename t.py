def priority(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > arr[max]:
            max = i
    item = arr[max]
    del arr[max]
    return item
ar = [1,12,3,1,4]
for i in range(len(ar)):
    print(priority(ar))