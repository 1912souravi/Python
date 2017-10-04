# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file = open("/Users/souravi/Documents/Python/romeo.txt",'r')
word_lst=[]
count=0
for line in file:
  line=line.rstrip()

  li=line.split()

  if li[0]=='From':
    word_lst.append(li[1])
    count+=1

print(sorted(word_lst))
print(count)
