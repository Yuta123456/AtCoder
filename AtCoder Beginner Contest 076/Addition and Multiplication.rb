n = gets.chomp.to_i
k = gets.chomp.to_i
ans = 1
for i in 0...n
    if ans * 2 > ans + k
        ans += k
    else
        ans *= 2
    end
end
print(ans)