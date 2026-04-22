#funcion crear un registro en tabla producto
#lista = productos
producto = []

#atributos de producto
#encabezasos id_producto categoria nombre precio_unitario
producto_1 = [1, "escritura", "lapiz negro HB",350]
producto_2 = [2, "escritura", "lapiz negro HB",50]
#1 registro -> una fila -> puede ser una lista

#armo la matriz
producto = [producto_1,producto_2
            ]
#acceder al precio de producto_1
print(producto_1[3])

for p in producto:
    print(p)
