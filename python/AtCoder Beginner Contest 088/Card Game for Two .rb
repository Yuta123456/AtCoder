n = gets.chomp.to_i
a = []
a = gets.chomp.split(" ").map(&:to_i)
a.sort!
a.reverse!
alice = 0
bob = 0
for i in 0...n
    if i % 2 == 0
        alice += a[i]
    else
        bob += a[i]
    end
end
print(alice - bob)