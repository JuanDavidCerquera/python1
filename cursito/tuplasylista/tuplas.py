# tuplas


tupla = ("perro", 23, 1.9, True)

print(type(tupla))
print(tupla[1])
print(tupla.index(23))

# tupla.pop()

# a diferencia de las lista esta no puede añadir ni remover elementos
# pero se puede modificar su tipo 


tupla = list(tupla)
print(type(tupla))

tupla.pop()
print(tupla)