a, b, c, d = gets.chomp.split.map(&:to_i)
ans = "No"
if (a - c).abs <= d
    ans = "Yes"
end
if a <= c and a <= b and b <= c
    if (b - a) <= d and (c - b) <= d
        ans = "Yes"
    end
end
if a >= c and c <= b and b <= a
    if (a - b) <= d and (b - c) <= d
        ans = "Yes"
    end
end
print(ans)