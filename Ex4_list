file = open("/Users/souravi/Documents/Python/romeo.txt",'r')
word_lst=[]
for line in file:
  line=line.rstrip()
  words=line.split()

  for word in words:
      if word in word_lst:
          continue
      else:
          word_lst.append(word)

print(sorted(word_lst))
