"""
SUPERMERCADO.py
Hacer un programa que calcule el flujo de caja de un supermercado.
cajas - cartas en efectivo
efectivo = [['1', [100, 1], [50, 13], [20, 5]],
            ['3', [50, 21], [20, 11], [10, 7], [0.02, 4]],
            ['2', [50, 2], [20, 9], [0.50, 12], [0.20, 13]]]
-cálculo importe por caja
-cálculo importe total
-impresión cantidad caja
-impresión cantidad total
"""

def flujo_caja_supermercado():
    efectivo = [['1', [100, 1], [50, 13], [20, 5]],
                ['3', [50, 21], [20, 11], [10, 7], [0.02, 4]],
                ['2', [50, 2], [20, 9], [0.50, 12], [0.20, 13]]]
    for caja in efectivo:
        numero_de_caja = caja[0]
        lista_dinero = caja[1]

        total_caja = 0

        for par in lista_dinero:
            print(total_caja)

        print(caja[0][0])

flujo_caja_supermercado()