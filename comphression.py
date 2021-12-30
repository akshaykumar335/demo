l1=[2*x for x in range(10) if x%2==0]
print(l1)
print(type(l1))
for y in l1:
    print(y)
print()
t1=(2*q for q in range(10) if q%2==0)
print(t1)
print(type(t1))
for z in t1:
    print(z)
print()
set={2*s for s in range(10) if s%2==0}
print(set)
print(type(set))
for p in set:
    print(p)
print()