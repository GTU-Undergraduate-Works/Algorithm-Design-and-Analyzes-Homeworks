def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(parent, i, j):
    a = find(parent,i)
    b = find(parent,j)
    parent[a] = b



def is_satisfiable(number_of_element, equality_constraint, inequality_constraints):
    parent = []
    for i in range(number_of_element):
        parent.append(i)


    for i in range(len(equality_constraints)):
        if find(parent, equality_constraint[i][0]) != find(parent,equality_constraint[i][1]):
            union(parent, equality_constraint[i][0], equality_constraint[i][1])

    for i in range(len(inequality_constraints)):
        if find(parent, inequality_constraints[i][0]) == find(parent,inequality_constraints[i][1]):
            return False
    return True

equality_constraints = [[0,1], [1,2], [2,3], [3,4]]
inequality_constraints = [[3,4]]
satisfiable = is_satisfiable(5, equality_constraints, inequality_constraints)
if satisfiable:
    print("Constraints can be satisfiable")
else:
    print("Constraints can not be satisfiable")