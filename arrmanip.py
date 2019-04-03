t=1,2,4,'@',"hello",7
l=[1,2,4,'@',"hello",7]
s={1,2,4,'@',"hello",7}
print(type(t),type(l),type(s),'\n')

s.add(-1j)
s.remove('@')
print(s)
s.pop()
print(s,'\n')

l.append(-1j)
l.remove('@')
l.insert(3,"$$$")
print(l)
l.pop()
print(l)
