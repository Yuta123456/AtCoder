a = gets.chomp.split.map(&:to_i)
if a.max() > 8
    print(":(")
else
    print("Yay!")
end

