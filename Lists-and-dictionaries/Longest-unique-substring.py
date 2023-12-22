def uniqueSubstring(string):
  '''Returns largest unique substring'''
  startL = 0
  endL = 0
  start = 0
  1 = len(string)
  while start<l:
    d = {string[start]: start}
    end = start+1
    while end<l and string[end] not in d:
      d[string[end]] = end
      end += 1
    if end-start > endL-startL:
      startL = start
      endL = end
    if end == 1:
      start = 1
    else:
      start = d[string[end]] + 1
  return string[startL:endL

# Main
S = input()
print(uniqueSubstring(s))
