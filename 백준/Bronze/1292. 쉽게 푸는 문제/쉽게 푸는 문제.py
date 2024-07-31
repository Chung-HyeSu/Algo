#1292
A,B = map(int,input().split())

def gen_arr(n):
    arr = []
    for i in range(1,n+1):
        arr.extend([i]*i)
    return arr

def get_sum(arr,st,ed):
    return sum(arr[st-1:ed])

a = gen_arr(A+B+1)
b = get_sum(a,A,B)
print(b)