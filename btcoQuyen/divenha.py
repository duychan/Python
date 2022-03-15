n = int(input())
listCostOfTickets = list(map(int,input().split()))
numberSV = int(input())
arr = []
def binary_search(left, right, arr, val):
      if val < arr[0]: return -1
      while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < val:
          left = mid + 1
        elif arr[mid] > val:
          right = mid - 1
        elif arr[mid] == val:
              return val
      return arr[right]
for _ in range(numberSV):
    balance = int(input())
    arr.append(balance)
for i in arr:
    print(binary_search(0,len(listCostOfTickets)-1, listCostOfTickets, i))
      