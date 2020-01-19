x,y,z = gets.chomp.split.map(&:to_i)
for i in 0..x
    if i * y + z * (i+1) > x
        print(i-1)
        exit()
    end
end
