from clases import html_PDF

block = input('Ingrese bloque de equipos: ')
numOrder = input('Ingrese número de orden: ')
enterprise = input('Ingrese nombre de empresa: ')
addressGathering = input('Ingrese dirección de empresa que va a entregar: ')
contact = input('Contacto que va a recibir: ')
phone = input('Telefono que va recibir: ')
dateGathering = f"Empresa entrega: {enterprise} Dirección: {addressGathering} <br>Contacto: {contact} <br>Phone: {phone}"
enterpriseDelivery =input('Ingrese empresa que va a recibir: ')
addressDelivery = input('Ingrese Dirección donde va a recibir: ')
dateDelivery = f"Empresa entrega: {enterpriseDelivery} Dirección: {addressDelivery}"
serial = "6CM94715BH (ISAH5675M)"

generator = html_PDF.ConvertPDF(block, numOrder, enterprise, addressGathering, contact, phone, enterpriseDelivery, addressDelivery, serial)
generator.generatePDF() 