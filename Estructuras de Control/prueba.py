alto = float(input())
ancho = float(input())
profundo = float(input())
volumen = float(alto*ancho*profundo)
costo = float(volumen*5)
iva = float()
print(costo)
if (alto > 30):
    costo = (costo + 2000.0)
if (costo > 10000.0):
    iva = (costo * 0.19)
print(volumen)
print(costo + iva)