a,b,c = gets.chomp.split(" ").map(&:to_i)
if a + b >= c
    print("Yes")
else
    print("No")
end