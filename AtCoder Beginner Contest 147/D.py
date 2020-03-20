def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    mod = 7 + 10**9
    leng = len(format(max(a), 'b'))
    bit_acc = [0 for i in range(leng)]
    for i in range(n):
        #先頭から二進数を0埋めした
        bit_data = format(a[i], 'b').zfill(leng)
        for j in range(leng):
            if bit_data[j] == '1':
                bit_acc[j] += 1
    ans = 0
    p = [pow(2,leng - 1 - j, mod) for j in range(leng)]
    for i in range(n):
        bit_data = format(a[i], 'b').zfill(leng)
        for j in range(leng):
            if bit_data[j] == '1':
                ans += (n - bit_acc[j]) * p[j]
            else:
                ans += bit_acc[j] * p[j]
            ans %= mod
    print((ans * 500000004) % mod)
if __name__ == "__main__":
    main() 


