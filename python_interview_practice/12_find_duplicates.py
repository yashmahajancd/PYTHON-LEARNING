lst = [1,2,2,3,4,4]
print(set([x for x in lst if lst.count(x) > 1]))