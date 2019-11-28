a,b,x = gets.chomp.split(" ").map(&:to_i)
if a + b >= x and a <= x 
    print("YES")
else
    print("NO")
end