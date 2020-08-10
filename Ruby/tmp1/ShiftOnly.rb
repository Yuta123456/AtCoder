def dev2(num)
  flag = true
  for i in 0..(num.length - 1)
      if(num[i] % 2 != 0)
          flag = false
      end
  end
  if(flag)
    for i in 0..(num.length - 1)
       num[i] = num[i] / 2
    end
  dev2(num)
  end
end

S = readlines
S  = fline.split(" ")
for i in 0..(S.length - 1)
    S[i] = S[i].to_i
end
dev2(S)
puts(num)
