require 'set'
s = gets.chomp.split("")
if Set.new(s).length == 3
    print("Yes")
else
    print("No")
end
