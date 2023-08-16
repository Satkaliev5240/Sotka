lst = []
for a in range(2,101):
    for b in range(2,101):
        lst.append(a**b)
new_list = sorted(list(set(lst)))
print(len(new_list))