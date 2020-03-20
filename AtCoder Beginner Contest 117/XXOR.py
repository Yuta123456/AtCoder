n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
bit_len = len(format(k, 'b'))
for i in range(n):
    bit_len = max(bit_len, len(format(a[i],'b')))
bit_count = [0 for i in range(bit_len)]
for i in range(n):
    bit = format(a[i], 'b').zfill(bit_len)
    for j in range(bit_len):
        if bit[j] == '1':
            bit_count[j] += 1
ans = 0
now_num = 0
for i in range(bit_len):
    if bit_count[i] < n - bit_count[i]:
        if now_num + 2 ** (bit_len - i - 1) <= k:
            now_num += 2 ** (bit_len - i - 1)
            ans += (n - bit_count[i]) * (2 ** (bit_len - i - 1))
            continue
    ans += bit_count[i] * (2 ** (bit_len - i - 1))
print(ans)