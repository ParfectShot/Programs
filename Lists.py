l1=['a','b','c']
l2=['b','d']

# Y stores the common elements of L1 and L2
y = [x for x in l1 and l2 if x in l1 and l2]
print("Common elements : " + str(y))

# Using set function to subtract items of l2 from l1 and printing them out directly
print("Elements in L1 and not in L2 : " + str(set(l1)-set(l2)))

