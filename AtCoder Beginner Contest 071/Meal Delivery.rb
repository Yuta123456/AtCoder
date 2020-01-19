x,a,b = gets.chomp.split.map(&:to_i)
if (a-x).abs > (b-x).abs
    print("B")
else
    print("A")
end