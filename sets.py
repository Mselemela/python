# my_set = {1, 2, 3, 4, 5}
# print(my_set)

# my_set.add(6)
# print(my_set)

# my_set.remove(3)
# print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# join two sets and remove duplicates
union_set = set1.union(set2)
print(union_set)

# Intersection find the common between sets
inter_set = set1.intersection(set2)
print(inter_set)

# Difference looks for values that are present in one set and not the other
diff_set = set1.difference(set2)
print(diff_set)