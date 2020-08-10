m = gets.chomp.to_f
km = m / 1000
if km < 0.1
    puts '00'
elsif km <= 5
    if km >= 1
        puts (km * 10).to_i
    else
        puts '0' + ((km * 10).to_i).to_s
    end
elsif km <= 30
    puts km.to_i + 50
elsif km <= 70
    puts ((km - 30) / 5 + 80).to_i
else
    puts '89' 
end
