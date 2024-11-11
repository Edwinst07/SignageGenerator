from clases import html_PDF
from clases import seriesFile
import numpy as np
import math

block = input('Ingrese bloque de equipos: ')
numOrder = input('Ingrese número de orden: ')
enterprise = input('Ingrese nombre de empresa: ')
addressGathering = input('Ingrese dirección de empresa que va a entregar: ')
contact = input('Nombre de contacto que va a recibir: ')
phone = input('Telefono que va recibir: ')
dateGathering = f"Empresa entrega: {enterprise} Dirección: {addressGathering} <br>Contacto: {contact} <br>Phone: {phone}"
enterpriseDelivery = input('Ingrese empresa que va a recibir: ')
addressDelivery = input('Ingrese Dirección donde va a recibir: ')
dateDelivery = f"Empresa entrega: {enterpriseDelivery} Dirección: {addressDelivery}"

filename = r'.\series.txt'
file = seriesFile.Series(filename)
"""
file =  open(filename, "r")
lines = np.array(file.read().split('\n'))
print("---------")
box1 = []
box2 = []
for serial in lines:  
    if (lines.tolist().index(serial)+1) % 2 == 0:
        box1.append(str(serial))
    else:
        box2.append(str(serial))
    

print(box1)
print(box2)

cantPages = math.ceil(lines.size/2)
"""

print(file.cantPages)
generator = html_PDF.ConvertPDF(block, numOrder, enterprise, addressGathering, contact, phone, enterpriseDelivery, addressDelivery, file.arraySeries1(), file.arraySeries2(), file.cantPages)
generator.generatePDF() 
