require 'set'
s = gets.chomp.split(//)
s = Set.new(s)
base = Set.new(('a'..'z').to_a)
if ((base-s).to_a).length == 0
    print("None")
else
    print((base-s).to_a[0])
end