def add(x, y):
    return x + y
result = add(3, 5)
print('penambahan')
print(result)

def minus (x, y):
    return x-y
result = minus(3,2)
print('pengurangan')
print(result)

def mult (x,y):
    return x*y
result = mult(3,3)
print('perkalian')
print(result)

def div (x,y):
    return x/y
result = div(5,2)
print('pembagian')
print(result)

def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == 'x':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)
    else:
        pass

expression_tree = ((2, '+', 3), 'x', (5, '-', 1))
result = tree(expression_tree)
print("hasil pohon ekspresi = ", result)
