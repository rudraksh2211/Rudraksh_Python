s={1,2,3,4,5,}
s1={"a","b","c","d","e"}
print(s)
print(s1)
s1.add("f")
print(s1)
print(s1.union(s))
print(s1.intersection(s))
print(s1.difference(s))
s2=set()
for i in range(5):
    s2.add(i)
print(s2)
s2.clear()
print(s2)