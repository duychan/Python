n1, n2, n3 = [int(i) for i in input().split()]
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
arr3 = [int(i) for i in input().split()]
arr1 = arr1[::-1]
arr2 = arr2[::-1]
arr3 = arr3[::-1]
arr1_new = [arr1[0]]
arr2_new = [arr2[0]]
arr3_new = [arr3[0]]
for i in range(1, len(arr1)):
    arr1_new.append(arr1_new[i - 1] + arr1[i])
for i in range(1, len(arr2)):
    arr2_new.append(arr2_new[i - 1] + arr2[i])
for i in range(1, len(arr3)):
    arr3_new.append(arr3_new[i - 1] + arr3[i])
maxVal = max(set(arr1_new).intersection(set(arr2_new), set(arr3_new)))
print(maxVal)