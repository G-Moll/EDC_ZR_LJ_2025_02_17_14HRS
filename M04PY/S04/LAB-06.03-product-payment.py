# 0603 SENTENCIAS CONDICIONALES

# Ejercicio 0603 (1.5 puntos)
#     - Una persona adquirió un producto para pagar en 20 meses.
#     - El primer mes pagó 10 €,
#     - el segundo 20 €,
#     - el tercero 40 €
#     - y así sucesivamente.
#         # Realizar un algoritmo para determinar
#         # cuánto debe pagar mensualmente
#         # y el total de lo que pagó después de los 20 meses.

base_payment = 10
current_payment = 0
total_payment = 0

for n in range( 1, 21 ):
    if n == 1:
        current_payment = base_payment
    else:
        current_payment = current_payment * 2
    total_payment += current_payment
    print( f"El pago del mes { n } es: ",  current_payment )

print( f"El pago total es { total_payment }")
