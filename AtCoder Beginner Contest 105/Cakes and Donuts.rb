n = gets.chomp.to_i
ans = "No"
for i in 0..n/4
    for j in 0..n
        if 4 * i + 7 * j == n
            ans = "Yes"
        elsif 4 * i + 7 * j > n
            break
        end
    end
end
puts ans

        
