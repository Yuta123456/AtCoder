a,b,k = gets.chomp.split(" ").map(&:to_i)
ans = []
if b - a < 2 * k
    ans = (a..b).to_a
else
    for i in 0..k-1
        ans.push(a + i)
    end
    for i in b-k+1..b
        ans.push(i)
    end
end
print(ans.join(" "))