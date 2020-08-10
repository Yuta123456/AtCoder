s1, e1 = gets.chomp.split.map(&:to_i)
s2, e2 = gets.chomp.split.map(&:to_i)
s3, e3 = gets.chomp.split.map(&:to_i)
puts s1 * e1 / 10 + s2 * e2 / 10 + s3 * e3 / 10 