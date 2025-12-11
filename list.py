L = [1,2,3,4,5,6]
print("Original List",L)

count = 0
for i in L:
    count = count + i

print("Sum of list : ",count)

Average = count/len(L)
print("Average : ",Average)

L.sort()
print("Sorted list : ",L)

print("Smallest Value : ",L[0])
print("Larges Value : ",L[-1])