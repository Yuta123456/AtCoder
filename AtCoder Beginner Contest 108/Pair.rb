k = gets.to_i
if k % 2 == 0
    k /= 2
    print(k ** 2)
else
    l = (k / 2).to_i
    k -= l
    print(k * l)
end