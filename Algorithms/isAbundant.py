n = int(input())

def is_abundant(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if sum > n:
        print(sum)
        return True
    return False

print(is_abundant(n))