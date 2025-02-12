# Nested lists in python
# Nested lists are lists that appear as elements in another list.


list1 = ['amar','akbar','antony','ram',56.78]
list2 = [23,34,25,56]

full_list = [list1,list2] # NESTED LISTS [ [LIST1], [LIST2] ]

print(full_list)

# 1D -ARRAY --- [23,45,67,878] -- SAME DATA TYPE ELEMENTS
# 2D - ARRAY --- [ [1,2,3], ['A', 'B', 'C']]
# 3D - ARRAY --- [[[0,1,2],[2,3,4],[4,5,6]],[3,5,6],[7,78,98]]


# USING NESTED INDEXING CONCEPT -- NESTED LISTS (2D -ARRAY)
name =full_list[0][1] # matrix concept
print(name)