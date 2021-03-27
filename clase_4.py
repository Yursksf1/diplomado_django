# Ejercicio de ejemplo
# teniendo el diccionario de pagos mensuales, define un algoritmo para calcular el pago que debes realizar mensualmente si solo debes pagar un tercio de los recibos sin incluir el internet

the_dictionary = { 'agua': 130000, 'luz': 150000, 'gas': 40000, 'internet': 90000 }

pago_yo = ['agua', 'gas', 'luz']
pago_total = 0

for key, value in the_dictionary.items():
    if key in pago_yo:
        pago_total = pago_total + (value*0.33)

print(pago_total)
