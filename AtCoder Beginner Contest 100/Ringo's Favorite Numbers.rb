d, n = gets.chomp.split.map(&:to_i)
if n == 100
    print( (100 ** d) * 101)
else    
    print((100 ** d) * n) 
end