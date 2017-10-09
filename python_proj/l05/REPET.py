a = ["Армен","человек шашлык","тор"]
print(a[0])
# a.append(input("добавь: "))
print(a)
a.insert(2,"халк")
print(a)
del a[1]
print(a)
a.remove("Армен")
print(a)
jl = ["Флэшка","чудо-женка"]
# a.extend(jl)
a += jl
print(a)