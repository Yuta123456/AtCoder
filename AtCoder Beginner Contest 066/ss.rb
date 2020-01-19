s = gets.chomp
for i in 1...s.length
    k = s.slice(0...(s.length-i))
    if k.length % 2 == 0
        if k.slice(0, k.length/2) == k.slice(k.length/2, k.length/2)
            print(s.length - i)
            exit()
        end
    end
end