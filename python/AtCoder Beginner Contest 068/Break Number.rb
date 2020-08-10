n = gets.chomp.to_i
for i in 0..n
    if 2**i > n
        print(2**(i- 1))
        exit()
    end
end