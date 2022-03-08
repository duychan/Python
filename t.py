def priority(arr):
    max = 0
    for i in range(len(arr)):
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