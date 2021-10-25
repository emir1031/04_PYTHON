s = input()
dict = {}
for i in s:
    dict[i] = s.count(i)
a = sorted(sorted(dict.items()), key=lambda x: x[1], reverse=True)
print(a)
for key,value in a[:3]:
  print(key,value)