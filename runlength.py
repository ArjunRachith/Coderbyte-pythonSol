def RunLength(str):
  index = 0
  counter = 0
  new_str = ''
  while index < len(str):
    if index+1 < len(str) and str[index+1] == str[index]:
      counter += 1
    else:
      new_str += "{}{}".format(counter+1, str[index])
      counter = 0
    index += 1
  return new_str
