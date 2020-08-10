k = []
a = gets.chomp.to_i
b = gets.chomp.to_i
c = gets.chomp.to_i
k.push([1,a])
k.push([2,b])
k.push([3,c])
k = k.sort{|x, y| y[1] <=> x[1]}
for i in [a,b,c]
    for j in 0...3
        if i == k[j][1]
            puts j+1
        end
    end
end