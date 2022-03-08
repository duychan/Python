def priority(arr):
    max = 0
    for i in range(len(arr)):
<<<<<<< HEAD
        if arr[i] < arr[max]:
            max = i
    item = arr[max]
    arr.pop(max)
    return item
ar = [1,12,13,12,3,1,4]
a = []
for i in range(len(ar)):
    a.append(priority(ar))
print(a)
=======
        if arr[i] > arr[max]:
            max = i
    item = arr[max]
    del arr[max]
    return item
ar = [1,12,3,1,4]
for i in range(len(ar)):
    print(priority(ar))
>>>>>>> 6aa056ac23397ebf8897093d7cf91f5387b3baf2
