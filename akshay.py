def longest_semi_repetative_substring(s):
  Left = 0
  max_length = 0
  seen = {}
  for right in range (len(s)):
    if s[right] in seen and seen [s(right)] >= left:
      left = seen [s(right)]+1
    seen[s(right)] = right
    max_length = max(max_length, right-left +1)
    


  return max_length

  s = "16255262"
  print(longest_semi_repetative_substring(s))