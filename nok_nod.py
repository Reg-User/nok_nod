"""
@author: reg_user
"""

def nok(a, b):
    list_x = (a, b)
    list_a = []
    list_b = []
    x_max = max(list_x, key = lambda i: int(i))
    x = range(1, x_max + 1)
    for n in x:
        list_a.append(n * a)
        list_b.append(n * b)
    min_x = list(set(list_a) & set(list_b))
    return min_x[0]

def nod(a, b):
    list_a = []
    list_b = []
    x_a = range(1, a + 1)
    x_b = range(1, b + 1)
    for n in x_a:
        if (a % n) == 0:
            list_a.append(n)
    for n in x_b:
        if (b % n) == 0:
            list_b.append(n)
            
    x = list(set(list_a) & set(list_b))
    return max(x, key = lambda i: int(i))

val_a = input("Enter your value a: ")
val_b = input("Enter your value b: ")        
print('Наименьшее общее кратное чисел ' + val_a + ' и ' + val_b + ' : ' + str(nok(int(val_a), int(val_b))))

print('Наибольший общей делитель чисел ' + val_a + ' и ' + val_b + ' : ' + str(nod(int(val_a), int(val_b))))

#print(np.lcm(int(val_a), int(val_b)))
