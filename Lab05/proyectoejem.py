cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1
final = len(cadena)
numero = float(cadena[inicio:final])
#print(inicio, final)
#print(cadena[inicio:final])
#print(type(cadena[inicio:final]))
print(type(numero))
