a = gets.chomp
if a == 'a'
    puts -1
else
    if a.length == 1
        puts 'a'
    else
        puts a.slice(0..-2)
    end
end