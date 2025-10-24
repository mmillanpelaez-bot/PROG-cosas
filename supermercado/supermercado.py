"""
SUPERMERCADO.py
Hacer un programa que calcule el flujo de caja de un supermercado.
cajas - cartas en efectivo
efectivo = [
    ['1', [100, 1], [50, 13], [20, 5]],
    ['3', [50, 21], [20, 11], [10, 7], [0.02, 4]],
    ['2', [50, 2], [20, 9], [0.50, 12], [0.20, 13]]
]
-cálculo importe por caja
-cálculo importe total
-impresión cantidad caja
-impresión cantidad total
"""

cajas = [
    ['1', [100, 1], [50, 13], [20, 5]],
    ['3', [50, 21], [20, 11], [10, 7], [0.02, 4]],
    ['2', [50, 2], [20, 9], [0.50, 12], [0.20, 13]]
]

def flujo_caja_supermercado(caja):
    total = 0

    for denom, qty in caja:
        numero_caja = caja[0]
        lista_dinero = caja[1]


        #for par in lista_dinero:
        #  print(total_caja)

        print(caja[1])