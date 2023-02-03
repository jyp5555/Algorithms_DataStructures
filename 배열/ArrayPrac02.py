# 주어진 길이 N의 int배열 arr에서 
# 합이 100인 서로 다른 위치의 두 원소가 존재하면 1을, 
# 존재하지 않으면 0을 반환하는 함수 
# func2(int arr[], int N)을 작성하라.

# O(n^2)
def func2(arr, N):
    for i in arr:
        if((100-i) in arr):
            return 1
        else: return 0

# O(n)
def fun2(arr, N):
    sum100 = [0 for i in range(101)]
    for i in arr:
        if(sum100[i] == 0):
            sum100[i] = 1
            if(sum100[100-i] == 1):
                return 1
    return 0

print(fun2([1,52,48],3))

        
